from flask import Blueprint, render_template
from database_service.controller.controller import Controller
database_route = Blueprint('database_route', __name__)

@database_route.route('/add/stops', methods=['POST'])
def add_stops():
    return Controller.add_stops()


@database_route.route('/get/stops/', methods=['GET'])
@database_route.route('/get/stops/<partiall_name>', methods=['GET'])
def get_all_stops(partiall_name = None):
    return Controller.get_all_stops(partiall_name)
@database_route.route('/add/bus', methods=['POST'])
def add_bus():
    return Controller.add_bus()
@database_route.route('/add/routes', methods=['POST'])
def add_routes():
    return Controller.add_routes()
@database_route.route('/delete/route', methods=['POST'])
def delete_route():
    return Controller.delete_route()
@database_route.route('/delete/schedule', methods=['POST'])
def delete_schedule():
    return Controller.delete_schedule()
@database_route.route('/get/schedule', methods=['POST'])
def get_schedule():
    return Controller.get_schedule()
@database_route.route('/add/route_stops', methods=['POST'])
def add_stops_in_route():
    return Controller.add_stops_in_route()
@database_route.route('/add/staff', methods=['POST'])
def add_staff():
    return Controller.add_staff()



    