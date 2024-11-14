from flask import Blueprint, render_template
from database_app.controller.controller import Controller
database_route = Blueprint('database_route', __name__)

@database_route.route('/database/stop', methods=['POST'])
def add_stops():
    return Controller.add_stops()
@database_route.route('/database/stop', methods=['GET'])
def get_stops():
    return Controller.get_stops()
@database_route.route('/database/stop', methods=['DELETE'])
def delelte_stops():
    return Controller.delete_stops()
@database_route.route('/database/bus', methods=['POST'])
def add_bus():
    return Controller.add_bus()
@database_route.route('/database/route', methods=['POST'])
def add_routes():
    return Controller.add_routes()
@database_route.route('/database/route', methods=['DELETE'])
def delete_route():
    return Controller.delete_route()
@database_route.route('/database/schedule', methods=['POST'])
def add_schedule():
    return Controller.add_schedule()
@database_route.route('/database/schedule', methods=['PUT'])
def delete_schedule():
    return Controller.delete_schedule()
@database_route.route('/database/schedule', methods=['GET'])
def get_schedule():
    return Controller.get_schedule()
@database_route.route('/database/ticket', methods=['POST'])
def book_offline_ticket():
    return Controller.book_offline_ticket()
@database_route.route('/database/route/addstop', methods=['POST'])
def add_stops_in_route():
    return Controller.add_stops_in_route()
@database_route.route('/database/reachtime', methods=['POST'])
def add_bus_stop_reach_time():
    return Controller.add_bus_stop_reach_time()
@database_route.route('/database/ticket', methods=['GET'])
def verify_ticket():
    return Controller.verify_ticket()
@database_route.route('/database/staff', methods=['POST'])
def add_staff():
    return Controller.add_staff()
@database_route.route('/database/staff', methods=['GET'])
def get_staff():
    return Controller.get_staff()



    