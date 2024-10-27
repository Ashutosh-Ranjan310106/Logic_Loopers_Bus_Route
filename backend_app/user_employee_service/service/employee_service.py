from db_utils.utils import cursor, connection  
from werkzeug.security import generate_password_hash, check_password_hash

class EmployeeService:
    def create_employee(user_name, official_email, password, phone_number, access_level_id,  first_name = None, last_name = None, salary = None):
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
        query = f'''
            INSERT INTO Employee ({coulmn}user_name, official_email, password, phone_number, access_level_id) 
            VALUES ({string}%s, %s, %s, %s, %s);
        '''
        print(query, values)
        try:
            cursor.execute(query,values+[user_name, official_email, hashed_password, phone_number, access_level_id])
            connection.commit()
            user_id = cursor.lastrowid
            return user_id
        except Exception as e:
            print(f"Error: {e}")
            return None
    @staticmethod
    def login_employee(official_email, password):
        query = "SELECT emp_id, password FROM Employee WHERE official_email = %s"
        try:
            cursor.execute(query, (official_email,))
            emp = cursor.fetchone()

            if emp and check_password_hash(emp["password"], password):
                return emp
            else:
                return -1
        except Exception as e:
            print(f"Error: {e}")
            return "An error occurred while logging in"