from db_utils.utils import get_cursor, get_connection, log_error
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib
import time
from datetime import datetime
import pytz
cursor = get_cursor()
connection = get_connection()
ist = pytz.timezone('Asia/Kolkata')

def generate_unique_key(user_id):
    hash_object = hashlib.sha256(f'{user_id}{time.time()}'.encode())
    return hash_object.hexdigest()
class EmployeeService:
    @staticmethod
    def create_employee(user_name, official_email, password, phone_number, access_level_id, employer_code, first_name = None, last_name = None, salary = None):
        hashed_password = generate_password_hash(password)
        print(password, hashed_password, str(employer_code) == '1234', employer_code)
        if str(employer_code) == '1234':
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
            query = f'''
                INSERT INTO Employee ({coulmn}user_name, official_email, password, phone_number, access_level_id) 
                VALUES ({string}%s, %s, %s, %s, %s);
            '''
            try:
                cursor.execute(query,values+[user_name, official_email, hashed_password, phone_number, access_level_id])
                connection.commit()
                emp_id = cursor.lastrowid
                return emp_id
            except Exception as e:
                connection.rollback()
                log_error("create employee",e)
                return e
    @staticmethod
    def login_employee(official_email, password, emp_ip):
        query = "SELECT emp_id, password FROM Employee WHERE official_email = %s"
        cursor.execute(query, [official_email])
        emp = cursor.fetchone()
        if emp and check_password_hash(emp["password"], password):
            query = "SELECT session_id FROM Emp_session WHERE emp_id = %s AND status = 1"
            cursor.execute(query, [emp["emp_id"]])
            active_session = cursor.fetchone()

            if active_session:
                return -3 

            query = '''
                    INSERT INTO Emp_session(emp_id, emp_ip, session_at) Values
                    (%s, %s, %s)
                    '''
            try:
                cursor.execute(query, (emp["emp_id"], emp_ip, datetime.now(ist)))
                session_id= cursor.lastrowid
                connection.commit()
                return session_id
            except Exception as e:
                connection.rollback()
                log_error('login employee',e)
                return -4
        else:
            if not emp:
                return -1
            return -2

    @staticmethod
    def logout_employee(emp_ip):
        print(emp_ip)
        query = '''
                 update emp_session set status = 0 where emp_ip = %s and status = 1;
                 '''

        try:
            cursor.execute(query, (emp_ip,))
            connection.commit()
            return 1
        except Exception as e:
            connection.rollback()
            log_error('logout employee', e)
            return -1
