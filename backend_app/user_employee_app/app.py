import sys, os
import json

sys.path.append(os.getcwd())
from user_employee_app.routes.routes import user_employee_route
from  db_utils.utils import *
from flask import Flask, jsonify
app = Flask(__name__)

app.register_blueprint(user_employee_route)

if __name__ == '__main__':
    app.run(debug=True, port=5002) # host = "192.168.228.145"


