import sys, os
import json

sys.path.append(os.getcwd())
from user_employee_app.routes.routes import user_employee_route
from  db_utils.utils import *
from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
from config import host
app.register_blueprint(user_employee_route)
CORS(app)
if __name__ == '__main__':
    app.run(host=host, port=5002) # host = "192.168.228.145"


