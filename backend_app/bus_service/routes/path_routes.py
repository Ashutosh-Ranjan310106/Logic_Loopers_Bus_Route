from flask import Blueprint, render_template
from bus_service.controller.path_controller import *

path_route = Blueprint('path_route', __name__)

@path_route.route('/buses/path', methods=['GET'])
def get_path_of_stop():
    return path_controller.get_path_of_stop()
    