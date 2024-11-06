from db_utils.utils import get_cursor, get_connection 
from datetime import datetime
cursor = get_cursor()
connection = get_connection()

class BusService: 
    @staticmethod
    def get_all_stops():
        query = f'''
            select * from 
            stops;
            '''
        cursor.execute(query)
        stops = cursor.fetchall()
        stops_dic = {}
        for stop in stops:
            stops_dic[stop["stop_id"]] = stop
        return stops_dic
    

    @staticmethod
    def get_all_routes():
        query = f'''
            select * from routes;
            '''
        cursor.execute(query)
        
        routes = cursor.fetchall()
        all_routes = {}
        for route in routes: all_routes["Route_id"] = route
        return all_routes
    
    @staticmethod
    def get_all_route_map():
        query = f'''
            select sir.*,st.*, rt.* from 
            Stops_In_Route sir
            join stops st on st.stop_id = sir.stop_id
            join routes rt on rt.route_id = sir.route_id
            order by sir.route_stop_number;
            '''
        cursor.execute(query)
        routes = cursor.fetchall()
        all_routes = {}
        for stop in routes:
            if stop["Route_id"] in all_routes:
                all_routes[stop["Route_id"]].append(stop)
            else:
                all_routes[stop["Route_id"]] = []
                all_routes[stop["Route_id"]].append(stop)
        return all_routes
    
    @staticmethod
    def get_bus_route(bus_number):
        query = f'''
            select * from 
            Stops_In_Route sir
            join Stops on Stops.stop_id = sir.stop_id
            join routes rt on sir.route_id = rt.route_id
            where rt.bus_no like "%{bus_number}"
            order by route_stop_number;
            '''
        cursor.execute(query)
        bus_route = cursor.fetchall()
        return bus_route
    
    @staticmethod
    def get_stops_in_routes(route_id):
        query = f'''
            select * from 
            Stops_In_Route sir
            where sir.route_id like "%{route_id}"
            order by route_stop_number;
            '''
        cursor.execute(query)
        route = cursor.fetchall()
        return route
    
    
    @staticmethod
    def get_recent_buses(stop_ids=None, stop_names=None, bus_number=None, after_time=None):
        if not after_time:
            after_time = datetime.now().time()
        if stop_ids[0]:
            parameter = 'st.stop_id IN (%s)' % ','.join(['%s'] * len(stop_ids))
            value = stop_ids
        elif stop_names[0]:
            parameter = 'st.stop_name IN (%s)' % ','.join(['%s'] * len(stop_names))
            value = stop_names
        if bus_number:
            parameter += 'add bus_no = %s'
            value.append(bus_number)
        recent_bus_query = f'''
            SELECT  stop_name, bsrt.time bus_time, bus_no, st.stop_id, sch.route direction
            FROM bus_stop_reach_time bsrt
            JOIN schedule sch ON sch.schedule_id = bsrt.schedule_id
            JOIN stops_in_route sir ON  bsrt.node_number = sir.route_stop_number and sch.route_id = sir.route_id
            JOIN routes rt ON rt.route_id = sch.route_id
            JOIN stops st ON sir.stop_id = st.stop_id
            where bsrt.time > %s  and {parameter}
            ORDER BY bsrt.time;
            '''
        cursor.execute(recent_bus_query, [after_time]+value)
        recent_buses = cursor.fetchall()
        bus_timing_map = {}
        for timing in recent_buses:
            stop_name = timing['stop_name']
            bus_time = timing['bus_time']
            bus_number = timing['bus_no']
            direction = timing['direction']
            if stop_name not in bus_timing_map:
                bus_timing_map[stop_name] = []
            bus_timing_map[stop_name].append([bus_time, bus_number, direction])
        return bus_timing_map
    
    