from config.config import cursor


class bus_service:
    def get_all_routes():
        query = f'''
            select route_id from routes;
            '''
        cursor.execute(query)
        route_ids = cursor.fetchall()
        query = f'''
            select * from 
            Stops_In_Route sir
            join Stops on Stops.stop_id = sir.stop_id
            join routes rt on sir.route_id = rt.route_id
            order by rt.route_id, route_stop_number;
            '''
        cursor.execute(query)
        routes = cursor.fetchall()
        all_routes = {}
        for route in routes:
            if route[3] in all_routes:
                all_routes[route[3]].append(route)
            else:
                all_routes[route[3]] = []
                all_routes[route[3]].append(route)
        print(all_routes)
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
    

