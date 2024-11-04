from bus_app.service.service import *
from bus_app.view.view import *
from flask import request

class BusController:
    def get_bus_routes():
        bus_number = request.args.get('bus_number')
        route = BusService.get_bus_route(bus_number)

        if route:
            return BusView.render_route(route)
        return BusView.render_error("no route found")

    def get_all_routes():
        all_routes = BusService.get_all_route_map()
        if all_routes:
            return BusView.render_all_routes(all_routes)
        return BusView.render_error("no route found")
    
    def get_recent_buses():
        stop_name = request.args.get('stop_name')
        stop_id = request.args.get('stop_id')
        if not stop_id and not stop_name:
            return BusView.render_error('incompleate query one parameter is required') 
        recent_buses = BusService.get_recent_buses([stop_id], [stop_name])
        if recent_buses:
            return BusView.render_recent_buses(recent_buses)
        return BusView.render_error("no recent buses")