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