python_executable = r"C:\Users\rrpra\OneDrive\Documents\GitHub\Logic_Loopers_Bus_Route\backend\venv\Scripts\python.exe"

import mysql.connector

# Establish a connection to the database
connection = mysql.connector.connect(
    host="localhost",        # Your host, e.g., "localhost"
    user="root",     # Your MySQL username
    password="password", # Your MySQL password
    database="bus_route"  # The name of the database you want to connect to
)

# Check if the connection is successful
if connection.is_connected():
    print("Successfully connected to the database")

# Create a cursor object to execute queries
cursor = connection.cursor(dictionary=True)