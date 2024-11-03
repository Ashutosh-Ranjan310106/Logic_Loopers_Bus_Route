from user_employee_service.service.user_service import user_service
from user_employee_service.view.view import View
from flask import render_template, request, jsonify
class user_controller:
    def get_all_links():
        return View.render_links()
    def create_user():
        data = request.get_json()
        name = data.get("name",'')
        email = data.get("email")
        gender = data.get("gender",'')
        phone_number = data.get("phone_number")
        password = data.get("password")
        if not email or not password:
            return View.render_error("Email and password are required"), 400
        user_id = user_service.create_user(name, email, gender, phone_number, password)
        if user_id:
            return View.render_success("user created successful", user_id)
        return View.render_error("email or phone number is alredy used")

    def login_user():
        data = request.get_json()
        email = data.get("email",'')
        phone_number = data.get("phone_number",'')
        password = data.get("password")
        user = user_service.login_user(email, phone_number, password)
        if not user:
            return View.render_error("email or phone number is incorrect")
        if user == -1:
            return View.render_error("incorrect password")
        return View.render_success("user logined", user["user_id"])
    def getfare():
        bus_number  = request.args.get('bus_number')
        starting_stop_number = request.args.get('starting_stop_number')
        ending_stop_number = request.args.get('ending_stop_number')
        category = request.args.get('category')
        print(bus_number, starting_stop_number, ending_stop_number, category)
        if not all([bus_number, starting_stop_number, ending_stop_number, category]):
            return View.render_error("Missing required parameters"), 400
        try:
            result = user_service.getfare(starting_stop_number, ending_stop_number, category, bus_number=bus_number)
            print(result)
            if result == -1:
                return View.render_error("Invalid route or stops"), 404
            return View.render_fare(result[0], bus_number, category, result[1]), 200
        except Exception as e:
            return View.render_error(str(e)), 500
        

    def book_ticket():
        data = request.get_json()
        user_id = data.get('user_id')
        route_id = data.get('route_id')
        starting_stop_number = data.get('starting_stop_number')
        ending_stop_number = data.get('ending_stop_number')
        gender = data.get('gender')
        category = data.get('category')

        price, route_id = user_service.getfare(starting_stop_number, ending_stop_number, category, route_id=route_id)
        if not all([user_id, route_id, starting_stop_number, ending_stop_number, price, gender, category]):
            return View.render_error("Missing required parameters"), 400
        try:
            ticket = user_service.book_online_tickets(user_id, route_id, starting_stop_number, ending_stop_number, price, gender, category)
            return View.render_ticket(ticket), 201
        except Exception as e:
            return View.render_error(str(e)), 500