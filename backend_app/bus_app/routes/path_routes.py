from flask import Blueprint, render_template
from bus_app.controller.path_controller import *

path_route = Blueprint('path_route', __name__)

@path_route.route('/buses/path', methods=['GET'])
def get_path_of_stop():
    
    return PathController.get_path_of_stop()
    