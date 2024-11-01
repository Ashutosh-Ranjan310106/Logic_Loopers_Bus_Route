from database_service.service.bus_service import BusService
from database_service.service.stop_service import StopService
from database_service.service.staff_service import StaffService
from database_service.service.routes_service import RouteService
from database_service.view.view import View
from database_service.view.stop_view import StopView
from database_service.view.schedule_view import ScheduleView
from flask import request
class Controller:
    def add_stops():
        if 'file' not in request.files:
            return View.render_error("No file part"), 400
        session_id = request.form.get("session_id")
        file = request.files['file']

        if file.filename == '':
            return View.render_error("No selected file"), 400
        result =  StopService.add_stop(file, session_id)
        if result == -1:
            return View.render_error("you are not allowed to upload to database")
        if result == 1:
            return View.render_success("upload successfull")
        return View.render_error("upload failed")
    
    def add_routes():
        if 'file' not in request.files:
            return View.render_error("No file part"), 400
        session_id = request.form.get("session_id")
        file = request.files['file']

        if file.filename == '':
            return View.render_error("No selected file"), 400
        result =  RouteService.add_route(file, session_id)
        if result == -1:
            return View.render_error("you are not allowed to upload to database")
        if result == 1:
            return View.render_success("upload successfull")
        return View.render_error("upload failed")
    
    def delete_route():
        
        bus_number = request.form.get("bus_number")
        session_id = request.form.get("session_id")
        
        result =  RouteService.delete_route(bus_number, session_id)
        if result == -1:
            return View.render_error("you are not allowed to edit database")
        if result == 1:
            return View.render_success("edit successfull")
        return View.render_error("edit failed")
    def delete_schedule():
        
        schedule_id = request.form.get("schedule_id")
        session_id = request.form.get("session_id")
        
        result =  BusService.delete_schedule(session_id, schedule_id,)
        if result == -1:
            return View.render_error("you are not allowed to edit database")
        if result == 1:
            return View.render_success("edit successfull")
        return View.render_error("edit failed")
    

    def get_schedule():
        
        bus_number = request.form.get("bus_number")
        session_id = request.form.get("session_id")
        
        result =  BusService.get_route_schedule(session_id, bus_number)
        if result == -1:
            return View.render_error("you are not allowed to view database")
        if result == -2:
            return View.render_error("no schedule found")
        if result:
            return ScheduleView.render_Schedule(result)
        return View.render_error("view failed")
    


    def add_stops_in_route():
        if 'file' not in request.files:
            return View.render_error("No file part"), 400
        bus_no = request.form.get("bus_no")
        session_id = request.form.get("session_id")
        file = request.files['file']

        if file.filename == '':
            return View.render_error("No selected file"), 400
        result =  RouteService.add_stops_in_route(bus_no, file, session_id)
        if result == -1:
            return View.render_error("you are not allowed to upload to database")
        if result == -2:
            return View.render_error("no route found")
        if result == 1:
            return View.render_success("upload successfull")
        return View.render_error("upload failed")
    
    def get_all_stops(partiall_name):
        stops =  StopService.get_all_stops(partiall_name)
        if stops:
            return StopView.render_stops(stops)
        return View.render_error("no stops found")

    def add_bus():
        result =  BusService.add_Bus()
        if result:
            return View.render_success("upload successfull")
        return View.render_error("upload failed")

    def add_staff():
        result =  StaffService.add_staff()
        if result:
            return View.render_success("upload successfull")
        return View.render_error("upload failed")