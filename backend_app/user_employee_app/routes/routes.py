from flask import Blueprint, render_template
from user_employee_app.controller.user_controller import UserController
from user_employee_app.controller.employee_controller import EmployeeController

user_employee_route = Blueprint('user_employee_route', __name__)
@user_employee_route.route('/')
def home():
    return UserController.get_all_links()


@user_employee_route.route('/user/create', methods=['POST'])
def create_user():
    return UserController.create_user()
@user_employee_route.route('/user/login', methods=['POST'])
def login_user():
    return UserController.login_user()
@user_employee_route.route('/user/logout', methods=['POST'])
def logout_user():
    return UserController.logout_user()
@user_employee_route.route('/user/fare', methods=['GET'])
def getfare():
    return UserController.getfare()
@user_employee_route.route('/user/ticket', methods = ['GET'])
def get_user_tickets():
    return UserController.get_user_tickets()
@user_employee_route.route('/user/ticket', methods = ['POST'])
def book_ticket():
    return UserController.book_ticket()
@user_employee_route.route('/employee/create', methods=['POST'])
def create_employee():
    return EmployeeController.create_employee()
@user_employee_route.route('/employee/login', methods=['POST'])
def login_employee():
    return EmployeeController.login_employee()
@user_employee_route.route('/employee/logout', methods=['POST'])
def logout_employee():
    return EmployeeController.logout_employee()


    