from flask import render_template

class BusView:
    def render_route(route, template = True):
        route_view={"Route_id":route[0]["Route_id"],"Bus_no":route[0]["bus_no"],"stop_list":[]}
        for stop in route:
            instance = {"route_stop_number":stop["route_stop_number"], "Fair_stage":stop["Fare_stage"], "Stop_Name":stop["stop_name"], "location_coordinate":stop["location_coordinate"]}
            route_view["stop_list"].append(instance)
        if template:
            return render_template('bus_route.html', bus_number=route[0]["bus_no"], route=route_view)
        return route_view
    def render_all_routes(routes):
        all_routes=[]
        for route_id in routes:
            all_routes.append(BusView.render_route(routes[route_id], template=False))
        return render_template('all_route.html', routes=all_routes)
    def render_error(msg, user_id=None):
        temp = {'error':msg}
        if user_id:
            temp['user_id'] = user_id
        return render_template('error.html', error_message=temp['error'])
    def render_recent_buses(recent_buses):

        formatted_data = {}
        for stop_name in recent_buses:
            formatted_data[stop_name] = []
            for bus_timing in recent_buses[stop_name]:
                formatted_data[stop_name].append({
                    "bus_time": str(bus_timing[0]),
                    "bus_no": bus_timing[1],
                    "direction":bus_timing[2]
                })
        return formatted_data