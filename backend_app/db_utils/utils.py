import json
from datetime import datetime
import os
python_executable = r"C:\Users\rrpra\OneDrive\Documents\GitHub\Logic_Loopers_Bus_Route\backend_app\venv\Scripts\python.exe"

import traceback
import mysql.connector

db_config = {'host':"localhost",
    'user':"root",     
    'password':"password", 
    'database':"bus_route" }
#connection = mysql.connector.connect(**db_config)





def get_connection_and_cursor():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    return connection, cursor

def close_connection_and_cursor(connection, cursor):
    connection.close()
    cursor.close()

def close_cursor(cursor):
    cursor.close()

def log_error(function, error):
    # Prepare the error entry
    tb = traceback.format_exc()
    file_name = os.path.join(os.path.dirname(os.getcwd()), "error_log.json")
    error_entry = {
        "function": function,
        "error": str(error),
        "traceback":str(tb),
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
