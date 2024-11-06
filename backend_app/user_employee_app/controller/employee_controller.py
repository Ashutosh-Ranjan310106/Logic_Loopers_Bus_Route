from user_employee_app.service.employee_service import EmployeeService
from user_employee_app.view.view import *
from flask import render_template, request
class EmployeeController:
    @staticmethod
    def create_employee():
        data = request.get_json()
        if not data:
            return View.render_error("No data provided"), 400

        user_name = data.get("user_name", "")
        first_name = data.get("first_name", "")
        last_name = data.get("last_name", "")
        official_email = data.get("official_email")
        password = data.get("password")
        phone_number = data.get("phone_number")
        access_level_id = data.get("access_level_id")
        salary = data.get("salary")
        user_id = EmployeeService.create_employee(user_name, official_email, password, phone_number, access_level_id,  first_name, last_name, salary)
        if user_id:
            return View.render_success("create successfull", user_id), 201
        return View.render_error("faild"), 200
    

    @staticmethod
    def login_employee():
        data = request.get_json()
        official_email = data.get("official_email")
        password = data.get("password")
        if not official_email or not password:
            return View.render_error("Email and password are required"), 400

        session_id = EmployeeService.login_employee(official_email, password)

        if session_id == -1:
            return View.render_error("employee not found"), 404
        elif session_id == -2:
            return View.render_error("wrong password"), 401
        elif session_id == -3:
            return View.render_error("Already logged in. Only one active session allowed."), 409

        return View.render_success("login succesfull", session_id), 200
    
    @staticmethod
    def logout_employee():
        data = request.get_json()
        session_id = data.get("session_id")

        session_id = EmployeeService.logout_employee(session_id)
        return View.render_success("logout succesfull", session_id), 200
        