from bus_service.service.path_service import *
from bus_service.view.view import *
from bus_service.view.path_view import *
from flask import render_template
class path_controller:

    def get_path_of_stop(stop1, stop2):
        path_of_stop = path_service.get_path_of_stop(stop1, stop2)
        if path_of_stop:
            path_of_stop =  path_view.render_path(path_of_stop)
            return render_template('bus_paths.html', paths=path_of_stop)
        return {"error":"error"}