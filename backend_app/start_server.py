import subprocess
import sys, os
sys.path.append(os.getcwd())
from  db_utils.utils import python_executable

def run_bus_service():
    subprocess.Popen([python_executable, "bus_app/app.py"])

def run_user_emloyee_service():
    subprocess.Popen([python_executable, "user_employee_app/app.py"])
def run_database_sevice():
    subprocess.Popen([python_executable, "database_app/app.py"])


if __name__ == '__main__':
    print("starting server (bus service, user service and employee service)")

    run_bus_service()
    run_user_emloyee_service()
    run_database_sevice()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nTerminating server. goodbye")
