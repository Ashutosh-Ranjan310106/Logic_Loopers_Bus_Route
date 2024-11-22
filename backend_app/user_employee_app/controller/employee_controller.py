from user_employee_app.service.employee_service import EmployeeService
from user_employee_app.view.view import *
from flask import render_template, request
from db_utils.utils import get_connection_and_cursor, close_connection_and_cursor

class EmployeeController:
    @staticmethod
    def create_employee():


        user_name = request.form.get("user_name", "")
        first_name = request.form.get("first_name", "")
        last_name = request.form.get("last_name", "")
        official_email = request.form.get("official_email")
        password = request.form.get("password")
        phone_number = request.form.get("phone_number")
        access_level_id = request.form.get("access_level_id")
        salary = request.form.get("salary")
        employer_code = request.form.get("employer_code")
        connection, cursor = get_connection_and_cursor()
        if not (user_name and official_email and password and phone_number and access_level_id and employer_code):
            return View.render_error('some parameters ar mising'), 400
        emp_id = EmployeeService.create_employee(user_name, official_email, password, phone_number, access_level_id, employer_code, first_name, last_name, salary, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if emp_id == -1:
            return View.render_error("incorrect or duplicate employee data"), 409
        if emp_id == -2:
            return View.render_error("incorrect employeer id"), 409
        return View.render_success("create successfull", emp_id), 201
        
    

    @staticmethod
    def login_employee():
        data = request.get_json()
        official_email = data.get("official_email")
        password = data.get("password")
        if not official_email or not password:
            return View.render_error("Email and password are required"), 400
        if 'X-Forwarded-For' in request.headers:
            emp_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        else:
            emp_ip = request.remote_addr
        connection, cursor = get_connection_and_cursor()
        session_id = EmployeeService.login_employee(official_email, password, emp_ip, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if session_id == -1:
            return View.render_error("employee not found"), 404
        elif session_id == -2:
            return View.render_error("wrong password"), 401
        elif session_id == -3:
            return View.render_error("Already logged in. Only one active session allowed."), 409

        return View.render_success("login succesfull", session_id), 200
    
    @staticmethod
    def logout_employee():
        if 'X-Forwarded-For' in request.headers:
            emp_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        else:
            emp_ip = request.remote_addr
        connection, cursor = get_connection_and_cursor()
        result = EmployeeService.logout_employee(emp_ip, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if result == 1:
            return View.render_success("logout succesfull"), 200
        if result == -1:
            return View.render_success("no login found"), 409
        if result == -2:
            return View.render_success("logout failed"), 500
        