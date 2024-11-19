import sys, os
import json
from flask_cors import CORS

sys.path.append(os.getcwd())
from database_app.routes.routes import database_route
from  db_utils.utils import *
from flask import Flask, jsonify
app = Flask(__name__)
from config import host
app.register_blueprint(database_route)
CORS(app)
if __name__ == '__main__':
    app.run(host=host,debug=True, port=5003) # host = "192.168.228.145"


