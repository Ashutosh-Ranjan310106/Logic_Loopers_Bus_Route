from flask import Blueprint, render_template
from database_service.controller.controller import Controller
database_route = Blueprint('database_route', __name__)

@database_route.route('/database/stop/add', methods=['POST'])
def add_stops():
    return Controller.add_stops()
@database_route.route('/database/stop/get', methods=['GET'])
def get_stops():
    return Controller.get_stops()
@database_route.route('/database/bus/add', methods=['POST'])
def add_bus():
    return Controller.add_bus()
@database_route.route('/database/route/add', methods=['POST'])
def add_routes():
    return Controller.add_routes()
@database_route.route('/database/route/delete', methods=['POST'])
def delete_route():
    return Controller.delete_route()
@database_route.route('/database/schedule/delete', methods=['POST'])
def delete_schedule():
    return Controller.delete_schedule()
@database_route.route('/database/schedule/get', methods=['POST'])
def get_schedule():
    return Controller.get_schedule()
@database_route.route('/database/ticket/add', methods=['POST'])
def book_offline_ticket():
    return Controller.book_offline_ticket()
@database_route.route('/database/route/addstop', methods=['POST'])
def add_stops_in_route():
    return Controller.add_stops_in_route()
@database_route.route('/database/ticket/get', methods=['GET'])
def verify_ticket():
    return Controller.verify_ticket()
@database_route.route('/database/staff/add', methods=['POST'])
def add_staff():
    return Controller.add_staff()



    