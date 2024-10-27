from flask import Blueprint, render_template
from bus_service.controller.path_controller import *

path_route = Blueprint('path_route', __name__)

@path_route.route('/buses/path/<int:stop1>/<int:stop2>', methods=['GET'])
def get_path_of_stop(stop1, stop2):
    return path_controller.get_path_of_stop(stop1, stop2)
    