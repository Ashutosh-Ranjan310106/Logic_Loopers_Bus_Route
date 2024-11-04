from flask import Blueprint, render_template
from bus_app.controller.controller import *

bus_route = Blueprint('bus_route', __name__)
@bus_route.route('/buses/routes', methods=['GET'])
def get_bus_routes():
    return BusController.get_bus_routes()  # assuming it returns a list of stops


@bus_route.route('/buses', methods=['GET'])
def get_all_routes():
    return BusController.get_all_routes()


@bus_route.route('/buses/recent_bus', methods=['GET'])
def get_recent_bus():
    return BusController.get_recent_buses()

    