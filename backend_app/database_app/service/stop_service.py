from db_utils.utils import get_connection, get_cursor, log_error
import pandas as pd
cursor = get_cursor()
connection = get_connection()
class StopService:
    @staticmethod
    def add_stop(file, session_id):
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

            df = pd.read_csv(file)
            parameter = ''
            values = []
            for index, row in df.iterrows():
                stop_name = row.get('stop_name')
                location_coordinate = row.get('location_coordinate')
                if pd.isna(stop_name): 
                    stop_name = None
                if pd.isna(location_coordinate): 
                    location_coordinate = None
                parameter += '(%s, %s), '
                values.extend([stop_name, location_coordinate])
            parameter = parameter.rstrip(', ')
            query = f'''
                INSERT INTO Stops (stop_name, location_coordinate) VALUES 
                {parameter} ;
            '''
            try:
                cursor.execute(query, values)
                connection.commit()
                return 1
            except Exception as e:
                connection.rollback()
                log_error('add stop', e)
                return e
        return -1
    

    @staticmethod
    def delete_stops(session_id, stop_ids):
        query = '''
                select acl.access_level_id acid from 
                Access_level acl
                join employee emp ON emp.access_level_id = acl.access_level_id
                join emp_session sesn ON sesn.emp_id = emp.emp_id
                where sesn.session_id = %s and sesn.status = 1; 
                '''
        cursor.execute(query, (session_id,))
        acc_level = cursor.fetchone()
        stop_list = ','.join(['%s']*len(stop_ids))
        if acc_level and acc_level['acid'] <= 1:
            query = f'''
                delete from Stops where stop_id in  {stop_list};
            '''
            try:
                cursor.execute(query, stop_ids)
                connection.commit()
                return 1
            except Exception as e:
                connection.rollback()
                log_error('delete stops', e)
                return e
        return -1
    @staticmethod
    def get_stops(partiall_name):
        if partiall_name:
            query = f"SELECT stop_name, stop_id FROM Stops where stop_name like \"{partiall_name}%\";"
        else:
            query = f"SELECT stop_name, stop_id FROM Stops;"
        cursor.execute(query)
        stops = cursor.fetchall()
        return stops