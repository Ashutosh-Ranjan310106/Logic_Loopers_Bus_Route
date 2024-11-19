from db_utils.utils import get_connection, get_cursor, log_error
import pandas as pd
cursor = get_cursor()
connection = get_connection()
class RouteService:
    @staticmethod
    def add_route(file, emp_ip):
        query = '''
                select acl.access_level_id acid from 
                Access_level acl
                join employee emp ON emp.access_level_id = acl.access_level_id
                join emp_session sesn ON sesn.emp_id = emp.emp_id
                where sesn.emp_ip = %s and sesn.status = 1; 
                '''
        cursor.execute(query, (emp_ip,))
        acc_level = cursor.fetchone()
        if acc_level and acc_level['acid'] <= 2:

            df = pd.read_csv(file)
            parameter = ''
            values = []
            for index, row in df.iterrows():
                bus_number = row.get('bus_number')
                avrage_duration = row.get('avrage_duration', '')
                number_of_stops = row.get('number_of_stops','')

                parameter += '(%s, %s, %s), '

                if pd.isna(avrage_duration): 
                    avrage_duration = None
                if pd.isna(number_of_stops): 
                    number_of_stops = None

                    
                values.extend([bus_number, avrage_duration, number_of_stops])
            parameter = parameter.rstrip(', ')
            query = f'''
                INSERT INTO Routes (bus_no, avg_Duration, number_of_stops) VALUES 
                {parameter} ;
            '''
            try:
                cursor.execute(query, values)
                connection.commit()
                return 1
            except Exception as e:
                log_error('add routes', e)
                return e
        return -1
    
    @staticmethod
    def delete_route(bus_number, emp_ip):
        query = '''
                select acl.access_level_id acid from 
                Access_level acl
                join employee emp ON emp.access_level_id = acl.access_level_id
                join emp_session sesn ON sesn.emp_id = emp.emp_id
                where sesn.emp_ip = %s and sesn.status = 1; 
                '''
        cursor.execute(query, (emp_ip,))
        acc_level = cursor.fetchone()
        if acc_level and acc_level['acid'] <= 1:
            query = f'''
                DELETE FROM Routes where bus_no = %s;
            '''
            try:
                cursor.execute(query, (bus_number,))
                connection.commit()
            except Exception as e:
                log_error('delete routes', e)
                return e
            return 1
        return -1
    
    @staticmethod
    def add_stops_in_route(bus_no,file, emp_ip):
        query = '''
                select acl.access_level_id acid from 
                Access_level acl
                join employee emp ON emp.access_level_id = acl.access_level_id
                join emp_session sesn ON sesn.emp_id = emp.emp_id
                where sesn.emp_ip = %s and sesn.status = 1; 
                '''
        cursor.execute(query, (emp_ip,))
        acc_level = cursor.fetchone()
        query = '''
                select route_id from 
                routes
                where bus_no = %s; 
                '''
        cursor.execute(query, (bus_no,))
        route = cursor.fetchone()
        if not route or not route['route_id']:
            return -2
        route_id = route['route_id']
        print(acc_level)
        if acc_level and acc_level['acid'] <= 2:

            query = "SELECT stop_name, stop_id FROM Stops;"
            cursor.execute(query)
            stop_mapping = {row['stop_name'].lower(): row['stop_id'] for row in cursor.fetchall()}

            df = pd.read_csv(file)
            parameter = ''
            values = []
            prev_fare_stage = 1
            for index, row in df.iterrows():
                stop_name = row.get('stop_name').lower() 
                route_stop_number = row.get('route_stop_number')
                fare_stage = row.get('fare_stage')
                if fare_stage or pd.isna(fare_stage):
                    fare_stage = prev_fare_stage
                else:
                    prev_fare_stage = fare_stage
                
                parameter += '(%s, %s, %s, %s), '
                values.extend([stop_mapping[stop_name], route_stop_number, fare_stage, route_id])
            

            query = f'''
                UPDATE stops_in_route sir
                join bus_stop_reach_time bsrt ON bsrt.route_id = sir.route_id and sir.route_stop_number=bsrt.node_number
                SET route_stop_number =  route_stop_number + %s, node_number = node_number + %s
                where route_stop_number >= %s and route_id = %s;
            '''
            cursor.execute(query, (index+1, index+1, values[1], route_id))


            parameter = parameter.rstrip(', ')
            query = f'''
                INSERT INTO stops_in_route (stop_id, route_stop_number, fare_stage, route_id) VALUES 
                {parameter} ;
            '''
            try:
                cursor.execute(query, values)
                connection.commit()
                return 1
            except Exception as e:
                log_error('add stops in routes', e)
                return e
        return -1