from bus_service.service import *
from bus_service.view import *

class bus_controller:
    def get_bus_routes(bus_number):
        route = bus_service.get_bus_route(bus_number)
        return bus_view.route_view(route)
    def get_all_routes():
        all_routes = bus_service.get_all_routes()
        return bus_view.all_route_view(all_routes)