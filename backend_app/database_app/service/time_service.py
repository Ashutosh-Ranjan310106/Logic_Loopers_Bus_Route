from db_utils.utils import log_error
import pandas as pd


class TimeService:

    @staticmethod
    def add_bus_stop_reach_time(file, emp_ip, connection, cursor):
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

                time =  row.get('time')
                node_number = row.get('node_number')
                schedule_id = row.get('schedule_id')
                if not (time and node_number and schedule_id):
                    return -2
                parameter += '(%s, %s, %s), '
                values.extend([time, node_number, schedule_id])
            parameter = parameter.rstrip(', ')
            query = f'''
                INSERT INTO  bus_stop_reach_time (time, node_number, schedule_id) VALUES 
                {parameter} ;
            '''
            try:
                cursor.execute(query, values)
                connection.commit()
                return 1
            except Exception as e:
                connection.rollback()
                log_error('add bus stop reach time', e)
                return e

        return -1
    @staticmethod
    def get_bus_stop_reach_time(connection, cursor):
        query = f'''SELECT  stop_name, bsrt.time bus_time, bus_no
            FROM bus_stop_reach_time bsrt
            JOIN schedule sch ON sch.schedule_id = bsrt.schedule_id
            JOIN stops_in_route sir ON  bsrt.node_number = sir.route_stop_number and sch.route_id = sir.route_id
            JOIN routes rt ON rt.route_id = sch.route_id
            JOIN stops st ON sir.stop_id = st.stop_id
            ORDER BY rt.route_id, bsrt.time;'''
        cursor.execute(query)
        stops = cursor.fetchall()
        return stops