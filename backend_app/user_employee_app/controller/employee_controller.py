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
        print("empcode", employer_code)
        user_id = EmployeeService.create_employee(user_name, official_email, password, phone_number, access_level_id, employer_code, first_name, last_name, salary)
        print("type",type(user_id) == int)
        if type(user_id) == int:
            return View.render_success("create successfull", user_id), 201
        return View.render_error("faild"+str(user_id)), 401
    

    @staticmethod
    def login_employee():
        official_email = request.form.get("official_email")
        password = request.form.get("password")
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
        session_id = request.form.get("session_id")

        session_id = EmployeeService.logout_employee(session_id)
        return View.render_success("logout succesfull", session_id), 200
        