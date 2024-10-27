from db_utils.utils import cursor  


class bus_service: 
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

    def get_all_routes():
        query = f'''
            select * from routes;
            '''
        cursor.execute(query)
        
        routes = cursor.fetchall()
        all_routes = {}
        for route in routes: all_routes["Route_id"] = route
        return all_routes
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
    
    