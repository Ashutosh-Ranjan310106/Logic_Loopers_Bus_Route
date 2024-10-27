from user_employee_service.service.user_service import user_service
from user_employee_service.view.view import view
from flask import render_template, request, jsonify
class user_controller:
    def get_all_links():
        return view.render_links()
    def create_user():
        data = request.get_json()
        name = data.get("name",'')
        email = data.get("email")
        gender = data.get("gender",'')
        phone_number = data.get("phone_number")
        password = data.get("password")
        if not email or not password:
            return view.render_error("Email and password are required"), 400
        user_id = user_service.create_user(name, email, gender, phone_number, password)
        if user_id:
            return view.render_successful("user created successful", user_id)
        return view.render_error("email or phone number is alredy used")

    def login_user():
        data = request.get_json()
        email = data.get("email",'')
        phone_number = data.get("phone_number",'')
        password = data.get("password")
        user = user_service.login_user(email, phone_number, password)
        if not user:
            return view.render_error("email or phone number is incorrect")
        if user == -1:
            return view.render_error("incorrect password")
        return view.render_successful("user logined", user["user_id"])