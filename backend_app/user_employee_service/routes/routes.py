from flask import Blueprint, render_template
from user_employee_service.controller.user_controller import user_controller
from user_employee_service.controller.employee_controller import employee_controller
from bus_service.routes.routes import *
from bus_service.routes.path_routes import *
user_employee_route = Blueprint('user_employee_route', __name__)
@user_employee_route.route('/')
def home():
    return user_controller.get_all_links()


@user_employee_route.route('/users/create', methods=['POST'])
def create_user():
    return user_controller.create_user()

@user_employee_route.route('/users/login', methods=['POST'])
def login_user():
    return user_controller.login_user()
@user_employee_route.route('/employee/create', methods=['POST'])
def create_employee():
    return employee_controller.create_employee()
@user_employee_route.route('/employee/login', methods=['POST'])
def login_employee():
    return employee_controller.login_employee()


    