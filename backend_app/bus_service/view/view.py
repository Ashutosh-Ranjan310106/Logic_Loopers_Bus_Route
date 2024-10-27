from flask import render_template

class bus_view:
    def render_route(route):
        route_view={"Route_id":route[0]["Route_id"],"Bus_no":route[0]["bus_no"],"stop_list":[]}
        for stop in route:
            instance = {"route_stop_number":stop["route_stop_number"], "Fair_stage":stop["Fare_stage"], "Stop_Name":stop["stop_name"], "location_coordinate":stop["location_coordinate"]}
            route_view["stop_list"].append(instance)
        return render_template('bus_route.html', bus_number=route[0]["bus_no"], route=route_view)
    def render_all_routes(routes):
        all_routes=[]
        print(routes)
        for route_id in routes:
            all_routes.append(bus_view.route_view(routes[route_id]))
        return render_template('all_route.html', routes=all_routes)
    def render_error(msg, user_id=None):
        temp = {'error':msg}
        if user_id:
            temp['user_id'] = user_id
        return render_template('error.html', error_message=temp['error'])
        
    