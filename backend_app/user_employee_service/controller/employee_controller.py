from user_employee_service.service.employee_service import *
from user_employee_service.view.view import *
from flask import render_template, request
class employee_controller:
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
            return View.render_successful("create successfull", user_id)
        return View.render_error("faild")

    def login_employee():
        data = request.get_json()
        official_email = data.get("official_email")
        password = data.get("password")
        
        # Validate the input
        if not official_email or not password:
            return View.render_error("Email and password are required"), 400

        # Call the EmployeeService's login_user method
        result = EmployeeService.login_employee(official_email, password)

        # Check if login was successful
        if result:
            # Here, you can return a success response or redirect the user as needed
            return View.render_successful("login succesfull", result["emp_id"]), 200
        else:
            return View.render_error("password wrong"), 401