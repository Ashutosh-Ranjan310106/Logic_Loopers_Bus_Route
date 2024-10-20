import sys, os
import json

sys.path.append(os.getcwd())
from bus_service.routes import bus_route
from  config.config import *
from flask import Flask, jsonify
app = Flask(__name__)

app.register_blueprint(bus_route)

if __name__ == '__main__':
    app.run(debug=True, port=5001) # host = "192.168.228.145"


