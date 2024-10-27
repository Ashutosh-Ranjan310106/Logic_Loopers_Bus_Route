from db_utils.utils import cursor, connection  
from werkzeug.security import generate_password_hash, check_password_hash

class user_service: 
    def create_user(name, email, gender, phone_number, password):
        hash_password = generate_password_hash(password)
        coulmn =''
        values = []
        if name:
            coulmn+='name, '
            values.append(name)
        if gender:
            coulmn+='gender, '
            values.append(gender)
        query = f'''
                    INSERT INTO Users ({coulmn}email, phone_number, password) 
                    VALUES ({'%s,'*len(values)} %s, %s, %s);
                '''
        print(query) 
        try:
            cursor.execute(query, values+[email, phone_number, hash_password])
            user_id = cursor.lastrowid
            connection.commit()
            return user_id
        except Exception as e:
            print("Error inserting user:", e)
            connection.rollback()
    

    def login_user(email, phone_number, password):
        query = '''
                select * from users
                where email = %s or phone_number = %s
                '''
        cursor.execute(query, (email, phone_number))
        user = cursor.fetchone()
        print(user['password'])
        if user:
            if check_password_hash(user['password'], password):
                return user
            else:
                return -1
    