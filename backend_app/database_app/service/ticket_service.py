from db_utils.utils import get_connection, get_cursor, log_error
import datetime
import pandas as pd
cursor = get_cursor()
connection = get_connection()

class TicketService:
    @staticmethod
    def book_offline_tickets(route_id, price, gender, category, direction, session_id):
        query = '''
                select acl.access_level_id acid from 
                Access_level acl
                join employee emp ON emp.access_level_id = acl.access_level_id
                join emp_session sesn ON sesn.emp_id = emp.emp_id
                where sesn.session_id = %s and sesn.status = 1; 
                '''
        cursor.execute(query, (session_id,))
        acc_level = cursor.fetchone()
        if acc_level and acc_level['acid'] <= 2:
            insert_ticket_query = '''
                INSERT INTO Tickets (route_id, price, gender, category, ticket_type, date_of_tickets)
                VALUES (%s, %s, %s, %s, %s, %s);
            '''

            cursor.execute(insert_ticket_query, (route_id, price, gender, category, 'offline', datetime.date.today()))
            

            ticket_id = cursor.lastrowid


            insert_offline_ticket_query = '''
                INSERT INTO Offline_Tickets (ticket_id, direction)
                VALUES (%s, %s);
            '''
            cursor.execute(insert_offline_ticket_query, (ticket_id, direction))
            

            connection.commit()
            

            get_ticket_query = '''
                SELECT t.ticket_id, t.route_id, t.price, t.gender, t.category, t.date_of_tickets, ot.direction
                FROM Tickets t
                JOIN Offline_Tickets ot ON t.ticket_id = ot.ticket_id
                WHERE t.ticket_id = %s;
            '''
            try:
                cursor.execute(get_ticket_query, (ticket_id,))
                connection.commit()
                ticket = cursor.fetchone()
            except Exception as e:
                connection.rollback()
                log_error('delete stops', e)
                return e
            return ticket
        return -1
    
    @staticmethod
    def verify_ticket(ticket_id, ticketdate, route_id):
        verify_ticket_query = '''
            SELECT ticket_id, route_id, price, gender, category, ticket_type, date_of_tickets
            FROM Tickets
        '''
        condition = []
        params = []
        if ticket_id:
            condition.append('ticket_id = %s and date_of_tickets = %s')
            params.extend([ticket_id, datetime.date.today()])
        if ticketdate:
            ticketdate = datetime.datetime.strptime(ticketdate, "%Y-%m-%d").date()
            condition.append('date_of_tickets = %s')
            params.append(ticketdate)
        if route_id:
            condition.append('route_id = %s')
            params.append(route_id)

        verify_ticket_query += 'WHERE ' + 'AND'.join(condition) + ';'
        cursor.execute(verify_ticket_query, params)
        ticket = cursor.fetchall()
        
        return ticket