from db_utils.utils import  log_error
import pandas as pd



class ScheduleService:
    @staticmethod
    def add_schedule(file, emp_ip, connection, cursor):

        query = '''
            SELECT acl.access_level_id AS acid 
            FROM Access_level acl
            JOIN employee emp ON emp.access_level_id = acl.access_level_id
            JOIN emp_session sesn ON sesn.emp_id = emp.emp_id
            WHERE sesn.emp_ip = %s AND sesn.status = 1;
        '''
        cursor.execute(query, (emp_ip,))
        acc_level = cursor.fetchone()

        if acc_level and acc_level['acid'] <= 2:
            df = pd.read_csv(file)
            parameter = ''
            values = []

            for _, row in df.iterrows():
                schedule_day = row.get('schedule_day')
                route = row.get('route')
                time = row.get('time')
                route_id = row.get('route_id')
                start_stop_number = row.get('start_stop_number')
                stop_stop_number = row.get('stop_stop_number')
                bus_id = row.get('bus_id')
                conductor_id = row.get('conductor_id')
                driver_id = row.get('driver_id')

                if not (schedule_day != None and route != None and time != None and route_id != None and start_stop_number != None and stop_stop_number != None and bus_id != None and conductor_id != None and driver_id != None):
                    return -2
                
                parameter += '(%s, %s, %s, %s, %s, %s, %s, %s, %s), '
                values.extend([schedule_day, route, time, route_id, start_stop_number, stop_stop_number, bus_id, conductor_id, driver_id])

            parameter = parameter.rstrip(', ')

            query = f'''
                INSERT INTO Schedule (schedule_day, route, time, route_id, start_stop_number, stop_stop_number, bus_id, conductor_id, driver_id) 
                VALUES {parameter};
            '''
            try:
                cursor.execute(query, values)
                connection.commit()
                return 1
            except Exception as e:
                connection.rollback()
                log_error('add schedule', e)
                return e
        return -1
    @staticmethod
    def delete_schedule(emp_ip, schedule_id, connection, cursor):
        query = '''
            SELECT acl.access_level_id AS acid 
            FROM Access_level acl
            JOIN employee emp ON emp.access_level_id = acl.access_level_id
            JOIN emp_session sesn ON sesn.emp_id = emp.emp_id
            WHERE sesn.emp_ip = %s AND sesn.status = 1;
        '''
        cursor.execute(query, (emp_ip,))
        acc_level = cursor.fetchone()
        if acc_level and acc_level['acid'] <= 2:
            query = '''
                DELETE FROM Schedule 
                WHERE schedule_id = %s;
            '''
            try:
                cursor.execute(query, (schedule_id,))
                connection.commit()
                if cursor.rowcount > 0:
                    return 1
                return -2
            except Exception as e:
                connection.rollback()
                log_error('delete schedule', e)
                return e 
        return -1

    @staticmethod
    def get_schedule(bus_number ,emp_ip, connection, cursor):
        query = '''
            SELECT acl.access_level_id AS acid 
            FROM Access_level acl
            JOIN employee emp ON emp.access_level_id = acl.access_level_id
            JOIN emp_session sesn ON sesn.emp_id = emp.emp_id
            WHERE sesn.emp_ip = %s AND sesn.status = 1;
        '''
        cursor.execute(query, (emp_ip,))
        acc_level = cursor.fetchone()

        if acc_level and acc_level['acid'] <= 2:

            

            query = f'''
                    select * from schedule
                    join routes ON schedule.route_id = routes.route_id
                    where bus_no = %s;
                '''
            cursor.execute(query, (bus_number,))
            schedule_data = cursor.fetchall()
            if not schedule_data:
                return -2
            return schedule_data
        return -1
    