from flask import Blueprint, render_template
from bus_service.controller.controller import *

bus_route = Blueprint('bus_route', __name__)
@bus_route.route('/buses/routes/<bus_number>', methods=['GET'])
def get_bus_routes(bus_number):
    return bus_controller.get_bus_routes(bus_number)  # assuming it returns a list of stops


@bus_route.route('/buses', methods=['GET'])
def get_all_bus():
    return bus_controller.get_all_routes()

    