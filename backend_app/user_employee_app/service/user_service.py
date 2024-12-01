from db_utils.utils import log_error
from werkzeug.security import generate_password_hash, check_password_hash
import datetime 

class UserService: 

    @staticmethod
    def create_user(name, email, gender, phone_number, password, connection, cursor):
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


        cursor.execute(query, values+[email, phone_number, hash_password])
        user_id = cursor.lastrowid
        connection.commit()
        return user_id

    
    @staticmethod
    def login_user(email, phone_number, password, user_ip, connection, cursor):
        query = '''
                select * from users
                where email = %s or phone_number = %s
                '''
        cursor.execute(query, (email, phone_number))
        user = cursor.fetchone()
        if user:
            if check_password_hash(user['password'], password):
                query = "SELECT user_log_id FROM user_log WHERE (user_ip = %s OR user_id = %s) AND status = 1"
                cursor.execute(query, (user_ip, user['user_id'],))
                active_session = cursor.fetchall()
                if active_session:
                    return -2 
                query = '''
                        insert into user_log(user_ip, user_id, status) values
                        (%s, %s, 1)
                        '''

                cursor.execute(query, (user_ip, user['user_id']))
                log_id = cursor.lastrowid
                    
                connection.commit()
                return log_id
                
                    

            else:
                return -1    

    @staticmethod
    def logout_user(user_ip, connection, cursor):
        check_query = "SELECT user_log_id FROM user_log WHERE user_ip = %s AND status = 1"
        cursor.execute(check_query, (user_ip,))
        active_session = cursor.fetchall()
        if not active_session:
            return -1
        query = '''
                update user_log set status = 0 where user_ip = %s and status = 1
                '''

        cursor.execute(query, (user_ip,))
        connection.commit()
        
        return 1
            

    @staticmethod
    def getfare(starting_stop_number, ending_stop_number, category, bus_number, connection, cursor):
        query = '''
                select * from stops_in_route sir
                join routes rt on  rt.route_id = sir.route_id
                join Bus_Type_Description
                where category = %s and  bus_no = %s and  (route_stop_number = %s or route_stop_number = %s)
                '''
        cursor.execute(query, (category, bus_number, starting_stop_number, ending_stop_number))

        stops_list = cursor.fetchall()
        if len(stops_list) != 2:
            
            return -1
        fs1 = stops_list[0]['Fare_stage']
        fs2 = stops_list[1]['Fare_stage']
        fsd = fs1 - fs2
        if fsd < 0:
            fsd = - fsd
        fare = stops_list[0]['base_fare'] + 5 * fsd
        
        return (fare, stops_list[0]['Route_id'])

    

    @staticmethod
    def get_user_tickets(user_ip, connection, cursor):
        check_user_query = '''
        select user_id from user_log
        where user_ip = %s and status = 1
        '''       
        cursor.execute(check_user_query, (user_ip,))
        user = cursor.fetchone()

        if not (user):
            return -1
        user_id = user['user_id']
        get_ticket_query='''
        select * from
        tickets tk join Online_tickets otk ON tk.ticket_id = otk.ticket_id
        join routes rt ON tk.route_id = rt.route_id 
        where user_id = %s
        '''
        cursor.execute(get_ticket_query, (user_id,))
        tickets = cursor.fetchall()
        
        return tickets
    

    @staticmethod
    def book_online_tickets(user_ip, route_id, starting_stop_number, ending_stop_number, price, gender, category, connection, cursor):
        check_user_query = '''
        select user_id from user_log
        where user_ip = %s and status = 1
        '''     
        cursor.execute(check_user_query, (user_ip,))
        user = cursor.fetchone()
        user_id = user['user_id']
        if not user_id:
            
            return -1
        insert_ticket_query = '''
        INSERT INTO Tickets (route_id, price, gender, category, ticket_type, date_of_tickets)
        VALUES (%s, %s, %s, %s, %s, %s);
        '''
        

        insert_online_ticket_query = '''
            INSERT INTO Online_Tickets (ticket_id, starting_stop_number, ending_stop_number, user_id, time_of_booking)
            VALUES (%s, %s, %s, %s, %s);
        '''
    
        cursor.execute(insert_ticket_query, (route_id, price, gender, category, 'online', datetime.date.today()))
        ticket_id = cursor.lastrowid
        cursor.execute(insert_online_ticket_query, (ticket_id, starting_stop_number, ending_stop_number, user_id, datetime.datetime.now().time()))
        connection.commit()
            
        return ticket_id
    