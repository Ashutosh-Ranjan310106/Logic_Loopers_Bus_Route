from bus_service.service.service import *
from bus_service.view.view import *
from flask import request

class bus_controller:
    def get_bus_routes():
        bus_number = request.args.get('bus_number')
        route = bus_service.get_bus_route(bus_number)

        if route:
            return bus_view.render_route(route)
        return bus_view.render_error("no route found")

    def get_all_routes():
        all_routes = bus_service.get_all_route_map()
        if all_routes:
            return bus_view.render_all_routes(all_routes)
        return bus_view.render_error("no route found")