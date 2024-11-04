from bus_app.service.path_service import *
from bus_app.view.view import *
from bus_app.view.path_view import *
from flask import render_template, request
class PathController:
    @staticmethod
    def get_path_of_stop():
        stop1 = int(request.args.get('stop1'))
        stop2 = int(request.args.get('stop2'))
        path_of_stop = PathService.get_path_of_stop(stop1, stop2)
        if path_of_stop:
            return PathView.render_path(path_of_stop), 200
            
        return BusView.render_error("no routes found"), 404