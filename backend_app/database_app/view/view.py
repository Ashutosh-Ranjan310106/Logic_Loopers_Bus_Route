from flask import render_template

class View:
    @staticmethod
    def render_success(message, user_id=None):
        r =  {
            "status": "success",
            "message": message,
        }
        if user_id:
            r["user_id"] = user_id
        return r

    @staticmethod
    def render_error(message):
        return {
            "status": "error",
            "message": message
        }

    
    @staticmethod
    def render_links():
        links = {'create_user':'http://127.0.0.1:5002/users/create','login_user':'http://127.0.0.1:5002/users/login', 'create_employee':'http://127.0.0.1:5002/employee', 'login_employee':'http://127.0.0.1:5002/employee', 'bus route by bus number':'http://127.0.0.1:5001/buses/routes/<bus_number>', 'all bus route':'http://127.0.0.1:5001/buses', 'path between stops':'http://127.0.0.1:5001/buses/path/<int:stop1>/<int:stop2>'}
        return links
    







    
    """
    @user_employee_route.route('/users/create', methods=['POST'])
def create_user():
    return user_controller.create_user()

@user_employee_route.route('/users/login', methods=['POST'])
def login_user():
    return user_controller.login_user()
@user_employee_route.route('/employee', methods=['POST'])
def create_employee():
    return employee_controller.create_employee()
@user_employee_route.route('/employee', methods=['get'])
def login_employee():
    return employee_controller.login_employee()


    from flask import Blueprint, render_template
from bus_service.controller.controller import *

bus_route = Blueprint('bus_route', __name__)
@bus_route.route('/buses/routes/<bus_number>', methods=['GET'])
def get_bus_routes(bus_number):
    return bus_controller.get_bus_routes(bus_number)  # assuming it returns a list of stops


@bus_route.route('/buses', methods=['GET'])
def get_all_bus():
    return bus_controller.get_all_routes()

    from flask import Blueprint, render_template
from bus_service.controller.path_controller import *

path_route = Blueprint('path_route', __name__)

@path_route.route('/buses/path/<int:stop1>/<int:stop2>', methods=['GET'])
def get_path_of_stop(stop1, stop2):
    return path_controller.get_path_of_stop(stop1, stop2)
    

make a starting root for these root where i can choice route
    """
    