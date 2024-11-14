import json
from datetime import datetime
import os
python_executable = r"C:\Users\rrpra\OneDrive\Documents\GitHub\Logic_Loopers_Bus_Route\backend_app\venv\Scripts\python.exe"

import mysql.connector

db_config = {'host':"localhost",
    'user':"root",     
    'password':"password", 
    'database':"bus_route" }
connection = mysql.connector.connect(**db_config)


if connection.is_connected():
    print("Successfully connected to the database")
    cursor = connection.cursor(dictionary=True)
else:
    print("data base connection failed")


def get_connection():
    return connection

def get_cursor():
    return cursor

def close_connection():
    connection.close()

def close_cursor():
    cursor.close()

def log_error(function, error):
    # Prepare the error entry
    file_name = os.path.join(os.path.dirname(os.getcwd()), "error_log.json")
    error_entry = {
        "function": function,
        "error": str(error),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Read existing log data if the file exists
    try:
        with open(file_name, "r") as f:
            error_log = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        error_log = []  # Start with an empty list if file doesn't exist or is invalid
    
    # Append the new error entry
    error_log.append(error_entry)
    
    # Write updated log back to the file
    with open(file_name, "w") as f:
        json.dump(error_log, f, indent=4)
