

class bus_view:
    def route_view(route):
        rt=[]
        for stop in route:
            instance = {"route_stop_number":stop[1], "Fair_stage":stop[2], "Stop_id":stop[4], "Stop_Name":stop[6], "location_coordinate":stop[7], "Route_id":stop[8], "Bus_no":stop[9]}
            rt.append(instance)
        return rt
    def all_route_view(routes):
        all_rt=[]
        for route in routes:
            print(route)
            rt={"Route_id":routes[route][0][8],"Bus_no":routes[route][0][9],"stop_list":[]}
            for stop in routes[route]:
                instance = {"route_stop_number":stop[1], "Fair_stage":stop[2], "Stop_id":stop[4], "Stop_Name":stop[6], "location_coordinate":stop[7]}
                rt["stop_list"].append(instance)
            all_rt.append(rt)
        return all_rt