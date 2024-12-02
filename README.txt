# Logic_Loopers_Bus_Route

# project name:-  Bus Route M
# Team Name :- Logic_Loopers

Team Members:-
  Ashutosh Ranjan (Team leader)
  Pankaj
  Aryan
  Tejasvi
  


Installation Steps
clone repository
Run "create_table_query.sql" to create database
Run "insert_data.sql" to insert data in  database
Run "get_data_query.sql" to get sample query output
to start server create virtual environment and activate it 
Install all module from requirment.txt
using where python get virtual python.exe link and replace it in backend_app/db_utils/utils.py  in variable python_executable
set you mysql password and user in backend_app/db_utils/utils
go to backend_app in terminal and run 'python start_server.py' to start backend server
go to frontend_app in terminal and run 'python app.py' to start frontend server





Bus Route Database Documentation


Overview

The Bus Route Database is designed to manage the operations of a bus transportation system (mainly city local bus like DTC BUS).
This database structure captures various aspects of the bus system, including bus types, users, stops, routes, tickets,
schedules, and staff, employee. The primary goal of this database is to facilitate effective management and tracking of bus operations.


Features of Our project 
1) Data Integrity: The database enforces data integrity through the use of primary keys, foreign keys, and unique constraints, ensuring that relationships between tables are maintained.

2) Comprehensive Ticket Management: The system effectively manages both online and offline tickets, allowing for clear tracking of ticket sales and validity

3) Dynamic Route Management: The database facilitates dynamic handling of routes and stops, enabling real-time updates to schedules and routes.

4) Reporting and Analysis: The structure allows for the generation of various reports, such as ticket sales, staff assignments, and bus schedules, aiding decision-making processes.

5) User Management: Detailed user records help in tracking customer demographics and preferences, which can inform marketing and operational strategies.

6) Employee Management: employee records with there level of access to database and who can do what in database

Tables & their relations


Tables:-
a. Buses: Represents all buses in the system, including their details.
b. Bus_stop_reach_time: Records the when buses reach stops.
c. Bus_Type_Description: Describes different types of buses available in the fleet.
d. Bus_type: Categorizes buses into different types based on specifications.
e. Offline_Tickets: clild entity of tickets Records details of tickets purchased offline.
f. Online_Tickets: clild entity of tickets Records details of tickets purchased online.
g. Routes: Defines various bus routes available in the system.
h. Schedule: Contains the schedules for bus departures and arrivals.
i. Staff: Represents all staff members involved in operations geralization of conductors and drivers tables.
j. Stops: Represents bus stops where passengers can board or alight.
k. Stops_in_route: Links stops to specific routes.
l. Tickets: Generalization of offline and  ticket information, including pricing and validity.
m. Users: Represents system users, including passengers and admin staff.
n. User_log: login log of user 
o. employee_session: employee login log of employee
p. employee: it store employee data such as its salay password username etc who are working on database or software.
q. access_level: it store how much employee have access to database or role of employee. 


Relationships:-
Bus_Type_Description is linked to Bus_type by category.
Bus_type is linked to Buses by Bus_type_id.
Users is linked to Online_Tickets and Offline_Tickets through User_id.
Stops_in_route is linked to Routes and Stops, establishing the connection between stops and routes.
Schedule connects Buses, Conductors, and Drivers, coordinating the operational aspects of bus schedules.
bus_stop_reach_time provides time tracking related to specific stops within a scheduled route.
tickets linked with category to provide detail for validity of ticket in buses
employee linked with access_level prodived details about access of employee to database



for testing we have taken following route map:-
Route 1:
[Stop a] -> [Stop b] -> [Stop c] -> [Stop d] -> [Stop e] -> [Stop f]

Route 2:
[Stop d] -> [Stop i] -> [Stop j] -> [Stop h] -> [Stop g]

Route 3:
[Stop c] -> [Stop i] -> [Stop k] -> [Stop g] -> [Stop f]



further improvement:- 
1) add qr codes to booktickets and verify tickets
2)we can add busroute map
3)we can add serilizibility
4) we can proper method to manage the offline tickets




