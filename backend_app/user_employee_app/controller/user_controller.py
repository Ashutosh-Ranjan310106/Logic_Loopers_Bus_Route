from user_employee_app.service.user_service import UserService
from user_employee_app.view.view import View
from flask import render_template, request, jsonify
from db_utils.utils import get_connection_and_cursor, close_connection_and_cursor
class UserController:

    @staticmethod
    def get_all_links():
        return View.render_links()
    
    @staticmethod
    def create_user():
        data = request.get_json()
        name = data.get("name",'')
        email = data.get("email")
        gender = data.get("gender",'')
        phone_number = data.get("phone_number")
        password = data.get("password")
        if not (email and password and phone_number):
            return View.render_error("Email, phone number and password are required"), 400
        connection, cursor = get_connection_and_cursor()
        user_id = UserService.create_user(name, email, gender, phone_number, password, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if user_id == -1:
            return View.render_error("email or phone is alredy used"), 409
        if user_id :
            return View.render_success("user created successful", user_id), 201
    
    @staticmethod
    def login_user():
        data = request.get_json()
        email = data.get("email",'')
        phone_number = data.get("phone_number",'')
        password = data.get("password")
        if 'X-Forwarded-For' in request.headers:
            user_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        else:
            user_ip = request.remote_addr
        connection, cursor = get_connection_and_cursor()
        user = UserService.login_user(email, phone_number, password, user_ip, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if not user:
            return View.render_error("email or phone number is incorrect"), 404
        if user == -1:
            return View.render_error("incorrect password"), 401
        if user == -2:
            return View.render_error("already loged in"), 401
        if user == -3:
            return View.render_error("error log in"), 401
        return View.render_success("user logined", user), 200
    @staticmethod
    def logout_user():
        if 'X-Forwarded-For' in request.headers:
            user_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        else:
            user_ip = request.remote_addr
        connection, cursor = get_connection_and_cursor()
        user = UserService.logout_user(user_ip, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if user == -1:
            return View.render_error("no login found"), 409
        if user == 1:
            return View.render_success("user logout success"), 200
        else:
            return View.render_error("internal error"), 500
    
    @staticmethod
    def getfare():
        bus_number  = request.args.get('bus_number')
        starting_stop_number = request.args.get('starting_stop_number')
        ending_stop_number = request.args.get('ending_stop_number')
        category = request.args.get('category')

        if not all([bus_number, starting_stop_number, ending_stop_number, category]):
            return View.render_error("Missing required parameters"), 400
        connection, cursor = get_connection_and_cursor()
        result = UserService.getfare(starting_stop_number, ending_stop_number, category, bus_number, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if result == -1:
            return View.render_error("Invalid route or stops"), 404
        if result == -2:
            return View.render_error("Internal error"), 500
        return View.render_fare(result[0], bus_number, category, result[1]), 200
    
    @staticmethod
    def get_user_tickets():
        if 'X-Forwarded-For' in request.headers:
            user_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        else:
            user_ip = request.remote_addr
        connection, cursor = get_connection_and_cursor()
        tickets = UserService.get_user_tickets(user_ip, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if tickets == -1:
            return View.render_error("you are not logined"), 401
        if tickets == -2:
            return View.render_error("internal error"), 500
        return View.render_tickets(tickets), 200


    @staticmethod
    def book_ticket():
        data = request.get_json()
        bus_number = data.get('bus_number')
        starting_stop_number = data.get('starting_stop_number')
        ending_stop_number = data.get('ending_stop_number')
        gender = data.get('gender')
        category = data.get('category')
        if 'X-Forwarded-For' in request.headers:
            user_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        else:
            user_ip = request.remote_addr
        connection, cursor = get_connection_and_cursor()
        result = UserService.getfare(starting_stop_number, ending_stop_number, category, bus_number, connection, cursor)
        if result == -1:
            close_connection_and_cursor(connection, cursor)
            return View.render_error("incorrect stop number")
        price, route_id = result
        if not all([user_ip, route_id, starting_stop_number, ending_stop_number, price, gender, category]):
            close_connection_and_cursor(connection, cursor)
            return View.render_error("Missing required parameters"), 400
        
        ticket = UserService.book_online_tickets(user_ip, route_id, starting_stop_number, ending_stop_number, price, gender, category, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if ticket == -1:
            return View.render_error("you are not logined"), 409
        if ticket == -2:
            return View.render_error("server error"), 500

        return View.render_success("ticket booked", ticket), 201