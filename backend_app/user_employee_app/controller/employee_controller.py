from user_employee_app.service.employee_service import EmployeeService
from user_employee_app.view.view import *
from flask import render_template, request
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
        user_id = EmployeeService.create_employee(user_name, official_email, password, phone_number, access_level_id, employer_code, first_name, last_name, salary)
        if type(user_id) == int:
            return View.render_success("create successfull", user_id), 201
        return View.render_error("faild"+str(user_id)), 401
    

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
            #return View.render_error("you are using vpn which is not allowed"), 409
        print(emp_ip)
        session_id = EmployeeService.login_employee(official_email, password, emp_ip)

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
        result = EmployeeService.logout_employee(emp_ip)
        if result == 1:
            return View.render_success("logout succesfull"), 200
        elif result == -1:
            return View.render_success("logout failed"), 500
        