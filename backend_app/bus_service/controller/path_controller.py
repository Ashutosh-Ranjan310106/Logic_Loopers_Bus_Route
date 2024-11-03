from bus_service.service.path_service import *
from bus_service.view.view import *
from bus_service.view.path_view import *
from flask import render_template, request
class path_controller:
    @staticmethod
    def get_path_of_stop():
        stop1 = int(request.args.get('stop1'))
        stop2 = int(request.args.get('stop2'))
        path_of_stop = PathService.get_path_of_stop(stop1, stop2)
        if path_of_stop:
            return path_view.render_path(path_of_stop), 200
            
        return bus_view.render_error("no routes found"), 404