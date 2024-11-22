from database_app.service.bus_service import BusService
from database_app.service.stop_service import StopService
from database_app.service.staff_service import StaffService
from database_app.service.routes_service import RouteService
from database_app.service.ticket_service import TicketService
from database_app.service.time_service import TimeService
from database_app.service.schedule_service import ScheduleService
from database_app.view.view import View
from database_app.view.ticket_view import TicketView
from database_app.view.stop_view import StopView
from database_app.view.schedule_view import ScheduleView
from flask import request
from db_utils.utils import get_connection_and_cursor, close_connection_and_cursor
class Controller:
    @staticmethod
    def add_stops():
        if 'file' not in request.files:
            return View.render_error("No file part"), 400
        if 'X-Forwarded-For' in request.headers:
            emp_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        else:
            emp_ip = request.remote_addr
        file = request.files['file']

        if file.filename == '':
            return View.render_error("No selected file"), 400
        connection, cursor = get_connection_and_cursor()
        result =  StopService.add_stop(file, emp_ip, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if result == -1:
            return View.render_error("you are not allowed to upload to database"), 403
        elif result == -2:
            return View.render_error("incorrect table formate"), 400
        if result == 1:
            return View.render_success("upload successfull"), 201
        return View.render_error(str(result)), 409
    @staticmethod
    def delete_stops():
        if 'X-Forwarded-For' in request.headers:
            emp_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        else:
            emp_ip = request.remote_addr
        stop_ids = request.form.get['stop_ids']
        connection, cursor = get_connection_and_cursor()
        result =  StopService.delete_stops(emp_ip, stop_ids, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if result == -1:
            return View.render_error("you are not allowed to upload to database"), 403
        elif result == -2:
            return View.render_error("incorrect table formate"), 400
        if result == 1:
            return View.render_success("upload successfull"), 201
        return View.render_error(str(result)), 409
    @staticmethod
    def add_routes():
        if 'file' not in request.files:
            return View.render_error("No file part"), 400
        if 'X-Forwarded-For' in request.headers:
            emp_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        else:
            emp_ip = request.remote_addr
        file = request.files['file']

        if file.filename == '':
            return View.render_error("No selected file"), 400
        connection, cursor = get_connection_and_cursor()
        result =  RouteService.add_route(file, emp_ip, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if result == -1:
            return View.render_error("you are not allowed to upload to database"), 403
        elif result == -2:
            return View.render_error("incorrect table formate"), 400
        if result == 1:
            return View.render_success("upload successfull"), 201
        return View.render_error(str(result)), 409
    @staticmethod
    def delete_route():
        
        bus_number = request.form.get("bus_number")
        if 'X-Forwarded-For' in request.headers:
            emp_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        else:
            emp_ip = request.remote_addr
        connection, cursor = get_connection_and_cursor()
        result =  RouteService.delete_route(bus_number, emp_ip, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if result == -1:
            return View.render_error("you are not allowed to edit database"), 403
        if result == 1:
            return View.render_success("edit successfull"), 201
        return View.render_error(str(result)), 409
    
    @staticmethod
    def add_schedule():
        if 'file' not in request.files:
            return View.render_error("No file part"), 400

        file = request.files['file']

        if file.filename == '':
            return View.render_error("No selected file"), 400
        if 'X-Forwarded-For' in request.headers:
            emp_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        else:
            emp_ip = request.remote_addr
        connection, cursor = get_connection_and_cursor()
        result =  ScheduleService.add_schedule(file, emp_ip, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if result == -1:
            return View.render_error("you are not allowed to upload to database"), 403
        if result == -2:
            return View.render_error("missing attributes"), 404
        if result == 1:
            return View.render_success("upload successfull"), 201
        return View.render_error(str(result)), 409
    

    @staticmethod
    def delete_schedule():
        
        schedule_id = request.form.get("schedule_id")
        if 'X-Forwarded-For' in request.headers:
            emp_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        else:
            emp_ip = request.remote_addr
        connection, cursor = get_connection_and_cursor()
        result =  ScheduleService.delete_schedule(emp_ip, schedule_id, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if result == -1:
            return View.render_error("you are not allowed to edit database"), 403
        if result == -2:
            return View.render_error("no schedule found"), 404
        if result == 1:
            return View.render_success("edit successfull"), 201
        return View.render_error(str(result)), 409
    
    @staticmethod
    def get_schedule():
        
        bus_number = request.args.get("bus_number")
        if 'X-Forwarded-For' in request.headers:
            emp_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        else:
            emp_ip = request.remote_addr
        connection, cursor = get_connection_and_cursor()
        result =  ScheduleService.get_schedule(bus_number, emp_ip, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if result == -1:
            return View.render_error("you are not allowed to view database"), 403
        if result == -2:
            return View.render_error("no schedule found"), 404
        if result:
            return View.render_success(ScheduleView.render_Schedule(result))
        return View.render_error("scedule view failed"), 409
    

    @staticmethod
    def add_stops_in_route():
        if 'file' not in request.files:
            return View.render_error("No file part"), 400
        bus_no = request.form.get("bus_no")
        if 'X-Forwarded-For' in request.headers:
            emp_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        else:
            emp_ip = request.remote_addr
        file = request.files['file']

        if file.filename == '':
            return View.render_error("No selected file"), 400
        connection, cursor = get_connection_and_cursor()
        result =  RouteService.add_stops_in_route(bus_no, file, emp_ip, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if result == -1:
            return View.render_error("you are not allowed to upload to database"), 403
        if result == -2:
            return View.render_error("no route found"), 404
        if result == -3:
            return View.render_error("incorrect details stop not found"), 404
        if result == 1:
            return View.render_success("upload successfull"), 201
        return View.render_error(str(result)), 409
    

    @staticmethod
    def get_stops():
        partial_name = request.args.get("partial_name")
        connection, cursor = get_connection_and_cursor()
        stops =  StopService.get_stops(partial_name, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if stops:
            return StopView.render_stops(stops), 200
        return View.render_error("no stops found"), 404
    
    @staticmethod
    def book_offline_ticket():        
        route_id = request.form.get('route_id')
        price = request.form.get('price')
        gender = request.form.get('gender')
        category = request.form.get('category')
        direction = request.form.get('direction')
        if 'X-Forwarded-For' in request.headers:
            emp_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        else:
            emp_ip = request.remote_addr
        connection, cursor = get_connection_and_cursor()
        ticket = TicketService.book_offline_tickets(route_id, price, gender, category, direction, emp_ip, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if ticket == -1:
            return View.render_error("you are not allowed to upload to database"), 403
        if type(ticket) == int:
            return View.render_success(ticket), 201
        return View.render_error(ticket), 409
    

    @staticmethod
    def add_bus():
        connection, cursor = get_connection_and_cursor()
        result =  BusService.add_bus(connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if result:
            return View.render_success("upload successfull"), 201
        return View.render_error("upload failed"), 409
    

    @staticmethod
    def add_staff():
        connection, cursor = get_connection_and_cursor()
        result =  StaffService.add_staff(connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if result:
            return View.render_success("upload successfull"), 201
        return View.render_error("upload failed"), 409
    

    @staticmethod
    def get_staff():
        connection, cursor = get_connection_and_cursor()
        result =  StaffService.get_staff(connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if result:
            return View.render_success("upload successfull"), 201
        return View.render_error("upload failed"), 409
    

    @staticmethod
    def add_bus_stop_reach_time():
        if 'file' not in request.files:
            return View.render_error("No file part"), 400
        if 'X-Forwarded-For' in request.headers:
            emp_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        else:
            emp_ip = request.remote_addr
        file = request.files['file']

        if file.filename == '':
            return View.render_error("No selected file"), 400
        connection, cursor = get_connection_and_cursor()
        result =  TimeService.add_bus_stop_reach_time(file, emp_ip, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if result == -1:
            return View.render_error("you are not allowed to upload to database"), 403
        elif result == -2:
            return View.render_error("incorrect table formate"), 400
        elif result == 1:
            return View.render_success("upload successfull"), 201
        return View.render_error(str(result)), 409
    
    
    @staticmethod
    def verify_ticket():
        ticket_id = request.args.get('ticket_id')
        date_of_tickets = request.args.get('ticketdate')
        route_id = request.args.get('route_id')
        connection, cursor = get_connection_and_cursor()
        tickets = TicketService.verify_ticket(ticket_id, date_of_tickets, route_id, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if tickets:
            return TicketView.render_ticket_verification(tickets), 200
        return View.render_error("Invalid or expired ticket"), 404