from db_utils.utils import log_error
import pandas as pd
import time
class RouteService:
    @staticmethod
    def add_route(file, route_data, emp_ip, connection, cursor):
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
            if file:
                df = pd.read_csv(file).iterrows()
            else:
                df = pd.Series(route_data)
            parameter = ''
            values = []
            for row in df:
                print(row)
                bus_number = row.get('bus_no')
                avrage_duration = row.get('avrage_duration', '')
                number_of_stops = row.get('number_of_stops','')
                total_number_of_trip = row.get('total_number_of_trip','')

                parameter += '(%s, %s, %s, %s), '

                if pd.isna(avrage_duration): 
                    avrage_duration = None
                if pd.isna(total_number_of_trip): 
                    total_number_of_trip = None

                    
                values.extend([bus_number, avrage_duration, number_of_stops, total_number_of_trip])
            parameter = parameter.rstrip(', ')
            print(query)
            query = f'''
                INSERT INTO Routes (bus_no, avg_Duration, number_of_stops, total_number_of_trip) VALUES 
                {parameter} ;
            '''
            cursor.execute(query, values)
            connection.commit()
            return 1
        return -1
    
    @staticmethod
    def delete_route(bus_number, emp_ip, connection, cursor):
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
            cursor.execute(query, (bus_number,))
            connection.commit()
        return -1
    
    @staticmethod
    def add_stops_in_route(bus_no,file, emp_ip, connection, cursor):
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
                select route_id, number_of_stops from 
                routes
                where bus_no = %s; 
                '''
        cursor.execute(query, (bus_no,))
        route = cursor.fetchone()
        if not route or not route['route_id']:
            return -2
        route_id = route['route_id']
        check_query = f'''
                select * from stops_in_route where route_id = %s; 
            '''
        cursor.execute(check_query, (route_id,))
        prev_data = cursor.fetchall()
        if prev_data:
            return -4
        if acc_level and acc_level['acid'] <= 2:
            df = pd.read_csv(file)

            stop_names = df['stop_name'].str.lower()
            stop_name_tuple = tuple(stop_names)
            if len(stop_name_tuple) != route['number_of_stops']:
                return -3
            query = f"SELECT stop_name, stop_id FROM Stops where stop_name IN ({','.join(['%s'] * len(stop_name_tuple))});"
            cursor.execute(query, stop_name_tuple)
            
            stop_mapping = {row['stop_name'].lower(): row['stop_id'] for row in cursor.fetchall()}
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
                stop_id = stop_mapping[stop_name]

                values.extend([stop_id, route_stop_number, fare_stage, route_id])
            parameter = parameter.rstrip(', ')
            query = f'''
                INSERT INTO stops_in_route (stop_id, route_stop_number, fare_stage, route_id) VALUES 
                {parameter} ;
            '''
            cursor.execute(query, values)
            connection.commit()
            return 1
        return -1