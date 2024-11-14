from db_utils.utils import get_connection, get_cursor, log_error
import pandas as pd
cursor = get_cursor()
connection = get_connection()


class ScheduleService:
    @staticmethod
    def add_schedule(file, session_id):
        # Query to check access level
        query = '''
            SELECT acl.access_level_id AS acid 
            FROM Access_level acl
            JOIN employee emp ON emp.access_level_id = acl.access_level_id
            JOIN emp_session sesn ON sesn.emp_id = emp.emp_id
            WHERE sesn.session_id = %s AND sesn.status = 1;
        '''
        cursor.execute(query, (session_id,))
        acc_level = cursor.fetchone()

        # Only proceed if access level is 2 or below
        if acc_level and acc_level['acid'] <= 2:
            # Load the CSV file into a DataFrame
            df = pd.read_csv(file)

            # Validate required columns in DataFrame
            required_columns = {'schedule_id', 'schedule_date', 'route', 'time', 'route_id', 'start_stop_number', 'stop_stop_number', 'bus_id', 'conductor_id', 'driver_id'}
            if not required_columns.issubset(df.columns):
                return -2

            # Prepare parameters for the SQL insert statement
            parameter = ''
            values = []

            for _, row in df.iterrows():
                schedule_id = row.get('schedule_id')
                schedule_date = row.get('schedule_date')
                route = row.get('route')
                time = row.get('time')
                route_id = row.get('route_id')
                start_stop_number = row.get('start_stop_number')
                stop_stop_number = row.get('stop_stop_number')
                bus_id = row.get('bus_id')
                conductor_id = row.get('conductor_id')
                driver_id = row.get('driver_id')
                
                # Build the parameter string and values list
                parameter += '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s), '
                values.extend([schedule_id, schedule_date, route, time, route_id, start_stop_number, stop_stop_number, bus_id, conductor_id, driver_id])

            # Remove the trailing comma and space from parameter string
            parameter = parameter.rstrip(', ')

            # Define the insert query
            query = f'''
                INSERT INTO Schedule (schedule_id, schedule_date, route, time, route_id, start_stop_number, stop_stop_number, bus_id, conductor_id, driver_id) 
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
        return -1  # Unauthorized access
    