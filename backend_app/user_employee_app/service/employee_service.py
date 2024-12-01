from db_utils.utils import get_connection_and_cursor, log_error
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib
import time
from datetime import datetime
import pytz
ist = pytz.timezone('Asia/Kolkata')

def generate_unique_key(user_id):
    hash_object = hashlib.sha256(f'{user_id}{time.time()}'.encode())
    return hash_object.hexdigest()
class EmployeeService:
    @staticmethod
    def create_employee(user_name, official_email, password, phone_number, access_level_id, emp_ip, first_name, last_name, salary, gender, connection, cursor):
        query = '''
                select acl.access_level_id acid from 
                Access_level acl
                join employee emp ON emp.access_level_id = acl.access_level_id
                join emp_session sesn ON sesn.emp_id = emp.emp_id
                where sesn.emp_ip = %s and sesn.status = 1; 
                '''
        cursor.execute(query, (emp_ip,))
        acc_level = cursor.fetchone()
        if acc_level and acc_level['acid'] == 0:
            hashed_password = generate_password_hash(password)
            coulmn =''
            values = []
            string=''
            if salary:
                coulmn+='salary, '
                values.append(salary)
                string+='%s, '
            if first_name:
                coulmn+='first_name, '
                values.append(first_name)
                string+='%s, '
            if last_name:
                coulmn+='last_name, '
                values.append(last_name)
                string+='%s, '
            if gender:
                coulmn+='gender, '
                values.append(gender)
                string+='%s, '
            query = f'''
                INSERT INTO Employee ({coulmn}user_name, official_email, password, phone_number, access_level_id) 
                VALUES ({string}%s, %s, %s, %s, %s);
            '''

            cursor.execute(query,values+[user_name, official_email, hashed_password, phone_number, access_level_id])
            connection.commit()
            emp_id = cursor.lastrowid
            return emp_id
        else:
            return -2
    @staticmethod
    def login_employee(official_email, password, emp_ip, connection, cursor):        
        query = "SELECT emp_id, password FROM Employee WHERE official_email = %s"
        cursor.execute(query, [official_email])
        emp = cursor.fetchone()
        if emp and check_password_hash(emp["password"], password):
            query = "SELECT session_id FROM Emp_session WHERE (emp_ip = %s OR emp_id = %s) AND status = 1"
            cursor.execute(query, (emp_ip, emp["emp_id"]))
            active_session = cursor.fetchall()

            if active_session:
                return -3 

            query = '''
                    INSERT INTO Emp_session(emp_id, emp_ip, session_at) Values
                    (%s, %s, %s)
                    '''

            cursor.execute(query, (emp["emp_id"], emp_ip, datetime.now(ist)))
            session_id= cursor.lastrowid
            connection.commit()
            return session_id
            
        else:
            if not emp:
                return -1
            return -2
    @staticmethod
    def logout_employee(emp_ip, connection, cursor):
        check_query = "SELECT * FROM emp_session WHERE emp_ip = %s AND status = 1"
        cursor.execute(check_query, (emp_ip,))
        active_session = cursor.fetchall()
        if not active_session:
            return -1
        query = '''
                update emp_session set status = 0 where emp_ip = %s and status = 1;
                '''


        cursor.execute(query, (emp_ip,))
        connection.commit()
        return 1
