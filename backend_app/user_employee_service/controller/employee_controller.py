from user_employee_service.service.user_service import *
from user_employee_service.view.view import *
from flask import render_template
class employee_controller:
    def get_bus_routes(bus_number):
        route = bus_service.get_bus_route(bus_number)

        if route:
            route = bus_view.route_view(route)
            return render_template('bus_route.html', bus_number=bus_number, route=route)
        return {"error":"error"}

    def get_all_routes():
        all_routes = bus_service.get_all_route_map()
        if all_routes:
            all_routes = bus_view.all_route_view(all_routes)
            return render_template('all_route.html', routes=all_routes)
        return {"error":"error"}