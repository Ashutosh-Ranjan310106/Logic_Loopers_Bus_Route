from db_utils.utils import get_cursor, get_connection  
from werkzeug.security import generate_password_hash, check_password_hash
import datetime 

cursor = get_cursor()
connection = get_connection()
class UserService: 

    @staticmethod
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
    
    @staticmethod
    def login_user(email, phone_number, password):
        query = '''
                select * from users
                where email = %s or phone_number = %s
                '''
        cursor.execute(query, (email, phone_number))
        user = cursor.fetchone()
        if user:
            if check_password_hash(user['password'], password):
                return user
            else:
                return -1
            

    @staticmethod
    def getfare(starting_stop_number, ending_stop_number, category, route_id=None, bus_number=None):
        if bus_number:
            query = '''
                    select * from stops_in_route sir
                    join routes rt on  rt.route_id = sir.route_id
                    join Bus_Type_Description
                    where category = %s and  bus_no = %s and  (route_stop_number = %s or route_stop_number = %s)
                    '''
            cursor.execute(query, (category, bus_number, starting_stop_number, ending_stop_number))
        else:
            query = '''
                    select * from stops_in_route sir
                    join Bus_Type_Description
                    where category = %s and  route_id = %s and  (route_stop_number = %s or route_stop_number = %s)
                    '''
            cursor.execute(query, (category, route_id, starting_stop_number, ending_stop_number))
        stops_list = cursor.fetchall()
        if len(stops_list) != 2:
            return -1
        fs1 = stops_list[0]['Fare_stage']
        fs2 = stops_list[1]['Fare_stage']
        fsd = fs1 - fs2
        if fsd < 0:
            fsd = - fsd
        fare = stops_list[0]['base_fare'] + 5 * fsd
        return fare, stops_list[0]['Route_id']
    

    @staticmethod
    def book_online_tickets(user_id, route_id, starting_stop_number, ending_stop_number, price, gender, category):
        insert_ticket_query = '''
        INSERT INTO Tickets (route_id, price, gender, category, ticket_type, date_of_tickets)
        VALUES (%s, %s, %s, %s, %s, %s);
        '''
        cursor.execute(insert_ticket_query, (route_id, price, gender, category, 'online', datetime.date.today()))

        ticket_id = cursor.lastrowid
        

        insert_online_ticket_query = '''
            INSERT INTO Online_Tickets (ticket_id, starting_stop_number, ending_stop_number, user_id, time_of_booking)
            VALUES (%s, %s, %s, %s, %s);
        '''
        cursor.execute(insert_online_ticket_query, (ticket_id, starting_stop_number, ending_stop_number, user_id, datetime.datetime.now().time()))
        connection.commit()

        get_ticket_query = '''
        SELECT t.ticket_id, t.route_id, t.price, t.gender, t.category, t.ticket_type, t.date_of_tickets, ot.starting_stop_number, ot.ending_stop_number, ot.user_id, ot.time_of_booking
        FROM  Tickets t
        JOIN  Online_Tickets ot ON t.ticket_id = ot.ticket_id
        WHERE t.ticket_id = %s;
        '''
        cursor.execute(get_ticket_query, (ticket_id,))
        ticket_details = cursor.fetchone()
        
        return ticket_details
    