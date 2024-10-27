from db_utils.utils import cursor  
import copy
class path_service:
    def printpath(path):
        for i in path:
            print(i)
    def rec(current_route, stop1, stop2, current_path, route_map, all_path, visited_routes):
        visited_routes.append(current_route)
        all_stop = route_map[current_route]
        direction = 0
        for i in range(len(all_stop)):
            if all_stop[i]['other_route_id'] == current_route:
                if direction == 0:
                    if all_stop[i]['stop_id'] == stop1:
                        path={"route":(all_stop[i]['bus_no'], 'up'),"stop_list":[]}
                        direction = 1
                        path["stop_list"].append(all_stop[i])
                else:
                    path["stop_list"].append(all_stop[i])
                    if all_stop[i]['stop_id'] == stop2:
                        all_path.append(current_path+[path])
                        return
            elif direction:
                if all_stop[i]['other_route_id'] not in visited_routes:
                    copy_path = copy.deepcopy(path)
                    if all_stop[i]["stop_id"] != copy_path["stop_list"][-1]["stop_id"]:

                        copy_path["stop_list"].append(all_stop[i+1])
                    path_service.rec(all_stop[i]['other_route_id'], all_stop[i]["stop_id"] ,stop2, current_path+[copy_path], route_map, all_path, visited_routes[::])
        direction = 0
        for i in range(len(all_stop)-1,-1,-1):
            if all_stop[i]['other_route_id'] == current_route:

                if direction == 0:
                    if all_stop[i]['stop_id'] == stop1:
                        path={"route":(all_stop[i]['bus_no'], 'down'),"stop_list":[]}
                        direction = 1
                        path["stop_list"].append(all_stop[i])
                else:
                    path["stop_list"].append(all_stop[i])
                    if all_stop[i]['stop_id'] == stop2:
                        all_path.append(current_path+[path])
                        return
            elif direction:
                if all_stop[i]['other_route_id'] not in visited_routes:
                    copy_path = copy.deepcopy(path)
                    if all_stop[i]["stop_id"] != copy_path["stop_list"][-1]["stop_id"]:

                        copy_path["stop_list"].append(all_stop[i-1])
                    path_service.rec(all_stop[i]['other_route_id'], all_stop[i]["stop_id"] ,stop2, current_path+[copy_path], route_map, all_path, visited_routes[::])
        visited_routes.pop()
        return None
   
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
    def get_routes_for_stop(stop_id):
        # Get all routes that pass through a particular stop (for transfers)
        query = f'''
            SELECT sir.route_id, sir.route_stop_number FROM Stops_In_Route sir
            WHERE sir.stop_id = "{stop_id}";
        '''
        cursor.execute(query)
        routes = cursor.fetchall()
        
        # Extract route_ids and return them
        return routes
    def get_path_of_stop(stop1, stop2):
        if stop1 == stop2:
            return []
        route_map = path_service.get_route_map()
        stop_route_id = path_service.get_routes_for_stop(stop1)
        all_path = []
        visited_routes = [rt["route_id"] for rt in stop_route_id]
        for rt in stop_route_id: 
            
            path = path_service.rec(rt["route_id"], stop1, stop2, [], route_map, all_path, visited_routes)

        return all_path