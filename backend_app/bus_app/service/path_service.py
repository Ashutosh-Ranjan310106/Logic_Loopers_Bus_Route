from db_utils.utils import get_cursor, get_connection  
import copy
import sys


cursor = get_cursor()
connection = get_connection()
cache_paths = {}
class PathService:
    @staticmethod
    def printpath(path):
        for i in path:
            print(i)

    @staticmethod
    def get_route_map():
        query = f'''
            select sir.*,st.stop_name, rt.bus_no , sir2.route_id other_route_id, sir2.route_stop_number other_route_stop_number from 
            Stops_In_Route sir
            join Stops_In_Route sir2 on sir.stop_id = sir2.stop_id
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
    def get_routes_for_stop(stop_id):

        query = f'''
            SELECT sir.route_id, sir.route_stop_number FROM Stops_In_Route sir
            WHERE sir.stop_id = "{stop_id}";
        '''
        cursor.execute(query)
        routes = cursor.fetchall()
        

        return routes
    
    @staticmethod
    def get_path_of_stop(stop1, stop2):
        if stop1 == stop2:
            return []
        max_depth = 3
        route_map = PathService.get_route_map()
        stop_route_id = PathService.get_routes_for_stop(stop1)
        
        queue = []
        all_path = []
        visited_routes = set(rt["route_id"] for rt in stop_route_id)
        visited_stops = {stop1}
        queue = [(rt["route_id"], stop1, [], visited_routes.copy()) for rt in stop_route_id[::-1]]


        while queue:
            current_route, current_stop, current_path, visited_routes = queue.pop(0)
            if (current_stop, stop2) in cache_paths:
                if len(current_path) < max_depth:
                    all_path.append(current_path + [cache_paths[(current_stop, stop2)]])
                continue

            

            all_stops = route_map[current_route]
            path = {"route": current_route,"direction":('up', all_stops[-1]["stop_name"]), "stop_list": []}
            found_path = False
            ch = False
            for i,stop in enumerate(all_stops):
                if stop['other_route_id'] == current_route:
                    if stop['stop_id'] == current_stop or ch:
                        ch = True
                        path["stop_list"].append(stop)
                        if stop['stop_id'] == stop2:
                            if len(current_path) < max_depth:
                                max_depth = len(current_path) + 1
                                all_path.append(current_path + [path])
                            found_path = True
                            cache_paths[(current_stop, stop2)] = path
                            break
                elif ch:
                    if stop['other_route_id'] not in visited_routes and stop['stop_id'] not in visited_stops:
                        visited_routes.add(stop['other_route_id'])
                        visited_stops.add(stop['stop_id'])
                        if len(current_path) < max_depth - 1:
                            queue.append((stop['other_route_id'], stop['stop_id'], current_path + [{"route":path["route"],"direction":('up',all_stops[-1]["stop_name"]), "stop_list":path["stop_list"].copy()}], visited_routes.copy()))
            
            if not found_path:
                path = {"route": current_route,"direction":('down',all_stops[0]["stop_name"]), "stop_list": []}
                ch = False
                for i, stop in enumerate(all_stops[::-1]):
                    if stop['other_route_id'] == current_route:
                        if stop['stop_id'] == current_stop or ch:
                            ch = True
                            path["stop_list"].append(stop)
                            if stop['stop_id'] == stop2:
                                if len(current_path ) < max_depth:
                                    max_depth = len(current_path) + 1
                                    all_path.append(current_path + [path])
                                found_path = True
                                cache_paths[(current_stop, stop2)] = path
                                break
                    elif ch:
                        if stop['other_route_id'] not in visited_routes and stop['stop_id'] not in visited_stops:                            
                            visited_routes.add(stop['other_route_id'])
                            visited_stops.add(stop['stop_id'])
                            if len(current_path) < max_depth - 1:
                                queue.append((stop['other_route_id'], stop['stop_id'], current_path + [{"route":path["route"],"direction":('down',all_stops[0]["stop_name"]), "stop_list":path["stop_list"][::]+[all_stops[i+1]]}], visited_routes.copy()))

            
            
        return all_path