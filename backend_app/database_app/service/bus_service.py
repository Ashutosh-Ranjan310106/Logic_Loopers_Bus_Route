from db_utils.utils import get_connection, get_cursor
cursor = get_cursor()
connection = get_connection()

class BusService:

    @staticmethod
    def delete_schedule(session_id, schedule_id):
        query = '''
                select acl.access_level_id acid from 
                Access_level acl
                join employee emp ON emp.access_level_id = acl.access_level_id
                join emp_session sesn ON sesn.emp_id = emp.emp_id
                where sesn.session_id = %s and sesn.status = 1; 
                '''
        cursor.execute(query, (session_id,))
        acc_level = cursor.fetchone()
        if acc_level and acc_level['acid'] <= 1:
            query = f'''
                DELETE FROM Schedule where schedule_id = %s;
            '''
            cursor.execute(query, (schedule_id,))
            connection.commit()
            return 1
        return -1
    @staticmethod
    def get_route_schedule(session_id, bus_number):
        query = '''
                select acl.access_level_id acid from 
                Access_level acl
                join employee emp ON emp.access_level_id = acl.access_level_id
                join emp_session sesn ON sesn.emp_id = emp.emp_id
                where sesn.session_id = %s and sesn.status = 1; 
                '''
        cursor.execute(query, (session_id,))
        acc_level = cursor.fetchone()
        if acc_level and acc_level['acid'] <= 3:
            query = f"SELECT sch.* FROM Schedule sch join Routes rt ON sch.route_id = rt.route_id where rt.bus_no = %s;"
            cursor.execute(query, (bus_number,))
            bus_schedule = cursor.fetchall()
            if bus_schedule:
                return bus_schedule
            return -2
        return -1