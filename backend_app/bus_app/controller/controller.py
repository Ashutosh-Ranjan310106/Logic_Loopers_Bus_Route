from bus_app.service.service import *
from bus_app.view.view import *
from flask import request
from db_utils.utils import get_connection_and_cursor, close_connection_and_cursor
class BusController:
    @staticmethod
    def get_bus_routes():
        bus_number = request.args.get('bus_number')
        connection, cursor = get_connection_and_cursor()
        route = BusService.get_bus_route(bus_number, connection, cursor)
        close_connection_and_cursor(connection, cursor)

        if route:
            return BusView.render_route(route), 200
        return BusView.render_error("no route found"), 404
    @staticmethod
    def get_all_routes():
        connection, cursor = get_connection_and_cursor()
        all_routes = BusService.get_all_route_map(connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if all_routes:
            return BusView.render_all_routes(all_routes), 200
        return BusView.render_error("no route found"), 404
    @staticmethod
    def get_recent_buses():
        stop_name = request.args.get('stop_name')
        stop_id = request.args.get('stop_id')
        if not stop_id and not stop_name:
            return BusView.render_error('incompleate query one parameter is required'), 400
        connection, cursor = get_connection_and_cursor()
        recent_buses = BusService.get_recent_buses([stop_id], [stop_name], connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if recent_buses:
            return BusView.render_recent_buses(recent_buses), 200
        return BusView.render_error("no recent buses"), 404