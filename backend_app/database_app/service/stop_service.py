from db_utils.utils import log_error
import pandas as pd
class StopService:
    @staticmethod
    def add_stop(file, emp_ip, connection, cursor):
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
            cursor.execute(query, values)
            connection.commit()
            return 1
        return -1
    

    @staticmethod
    def delete_stops(emp_ip, stop_ids, connection, cursor):
        query = '''
                select acl.access_level_id acid from 
                Access_level acl
                join employee emp ON emp.access_level_id = acl.access_level_id
                join emp_session sesn ON sesn.emp_id = emp.emp_id
                where sesn.emp_ip = %s and sesn.status = 1; 
                '''
        cursor.execute(query, (emp_ip,))
        acc_level = cursor.fetchone()
        stop_list = ','.join(['%s']*len(stop_ids))
        if acc_level and acc_level['acid'] <= 1:
            query = f'''
                delete from Stops where stop_id in  {stop_list};
            '''
            cursor.execute(query, stop_ids)
            connection.commit()
            return 1
        return -1
    @staticmethod
    def get_stops(partiall_name, connection, cursor):
        if partiall_name:
            query = f"SELECT stop_name, stop_id FROM Stops where stop_name like \"%{partiall_name}%\";"
        else:
            query = f"SELECT stop_name, stop_id FROM Stops;"
        cursor.execute(query)
        stops = cursor.fetchall()
        return stops