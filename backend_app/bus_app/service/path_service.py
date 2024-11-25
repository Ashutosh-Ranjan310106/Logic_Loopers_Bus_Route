from db_utils.utils import log_error
import copy
import sys
from bus_app.service.service import BusService


cache_paths = {}
class PathService:

    @staticmethod
    def get_route_map(connection, cursor):
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
    def get_routes_for_stop(stop_id, connection, cursor):

        query = f'''
            SELECT sir.route_id, sir.route_stop_number FROM Stops_In_Route sir
            WHERE sir.stop_id = "{stop_id}";
        '''
        cursor.execute(query)
        routes = cursor.fetchall()
        

        return routes
    
    @staticmethod
    def get_path_of_stop(stop1, stop2, connection, cursor):
        try:
            if stop1 == stop2:
                return []
            max_depth = 3
            route_map = PathService.get_route_map(connection, cursor)
            stop_route_id = PathService.get_routes_for_stop(stop1, connection, cursor)
            
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
                                    queue.append((stop['other_route_id'], stop['stop_id'], current_path + [{"route":path["route"],"direction":('down',all_stops[0]["stop_name"]), "stop_list":path["stop_list"][::]}], visited_routes.copy()))

                
                
            return PathService.process_path(paths=all_path, connection=connection, cursor=cursor)
        except Exception as e:
            log_error(f"get path of stop {stop1, stop2}", e)
            return -1
        

    @staticmethod
    def process_path(paths, connection, cursor):
        if not paths: return 
        processed_paths = []
        for path in paths:
            total_stops = 0
            changes = len(path)
            total_ac_fare = 0
            total_non_ac_fare = 0
            starting_stops_list = []
            for sub_path in path:
                stops_count = len(sub_path['stop_list'])
                total_stops += stops_count
                current_fare_stage = sub_path['stop_list'][0]["Fare_stage"]
                sub_path['bus_no'] = sub_path['stop_list'][0]["bus_no"]
                starting_stops_list.append(sub_path['stop_list'][0]["stop_id"])
                # Initial fare stages for each sub-path
                total_ac_fare += 10  # Base fare for AC
                total_non_ac_fare += 5  # Base fare for non-AC

                for stop in sub_path['stop_list']:
                    fare_stage = stop["Fare_stage"]
                    

                    # Accumulate fares for the path
                    total_ac_fare += abs(fare_stage - current_fare_stage) * 5
                    total_non_ac_fare += abs(fare_stage - current_fare_stage) * 5
                    current_fare_stage = fare_stage

            

            bus_timings = BusService.get_recent_buses(stop_ids=starting_stops_list, connection=connection, cursor=cursor, after_time='00:00:00')
            for index, sub_path in enumerate(path):
                if sub_path['stop_list'][0]['stop_name']  not in  bus_timings:
                    sub_path['bus_timings'] = 'no timings are available now '
                else:
                    sub_path['bus_timings']=[]
                    for timing in bus_timings[sub_path['stop_list'][0]['stop_name']]:
                        if timing[2] == sub_path['direction'][0]:
                            sub_path['bus_timings'].append(str(timing[0]))
            
            
            processed_paths.append({
                "route": path,
                "summary": {
                    "changes": changes - 1,
                    "total_stops": total_stops,
                    "total_ac_fare": total_ac_fare,
                    "total_non_ac_fare": total_non_ac_fare
                }
            })
        
        return processed_paths