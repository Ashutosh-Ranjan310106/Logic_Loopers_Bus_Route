from bus_app.service.path_service import *
from bus_app.view.view import *
from bus_app.view.path_view import *
from flask import render_template, request
from db_utils.utils import get_connection_and_cursor, close_connection_and_cursor
class PathController:
    @staticmethod
    def get_path_of_stop():
        stop1 = int(request.args.get('stop1'))
        stop2 = int(request.args.get('stop2'))
        connection, cursor = get_connection_and_cursor()
        path_of_stop = PathService.get_path_of_stop(stop1, stop2, connection, cursor)
        close_connection_and_cursor(connection, cursor)
        if path_of_stop ==-1:
            return BusView.render_error('internal error'), 500
        if path_of_stop:
            return PathView.render_path(path_of_stop), 200
            
        return BusView.render_error("no routes found"), 404