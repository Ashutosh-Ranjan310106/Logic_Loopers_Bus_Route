from flask import Blueprint
from bus_service.controller import *

bus_route = Blueprint('bus_route', __name__)
@bus_route.route('/buses/routes/<bus_number>', methods=['GET'])
def get_bus_routes(bus_number):
    return bus_controller.get_bus_routes(bus_number)

@bus_route.route('/buses', methods=['GET'])
def get_all_bus():
    return bus_controller.get_all_routes()
    