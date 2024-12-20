import sys, os
import json
from flask_cors import CORS
sys.path.append(os.getcwd())
from bus_app.routes.routes import bus_route
from bus_app.routes.path_routes import path_route
from  db_utils.utils import *
from flask import Flask, jsonify
app = Flask(__name__)
from config import host
CORS(app)
app.register_blueprint(bus_route)
app.register_blueprint(path_route)

if __name__ == '__main__':
    app.run(host=host, debug=True, port=5001)


