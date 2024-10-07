
DROP DATABASE Bus_Route;
CREATE DATABASE Bus_Route;
USE Bus_Route;
CREATE TABLE Bus_type (
    Bus_type_id INT PRIMARY KEY,
    Capacity INT,
    Base_fare INT NOT NULL
);

CREATE TABLE Users (
    User_id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100),
    Gender ENUM('male', 'female') default 'male',
    phone_number VARCHAR(12) NOT NULL
);
CREATE TABLE Stop_Location_Name(
	location_coordinate VARCHAR(50) PRIMARY KEY,
	location_name VARCHAR(100) NOT NULL
);
CREATE TABLE Stops (
    Stop_id INT PRIMARY KEY,
    Stop_Name VARCHAR(50),
    location_coordinate VARCHAR(50) ,
    foreign key(location_coordinate) REFERENCES Stop_Location_Name(location_coordinate)
);


CREATE TABLE Routes (
    Route_id INT PRIMARY KEY,
    Bus_no VARCHAR(10),
    Avg_Duration TIME,
    number_of_stops INT
);

CREATE TABLE Tickets (
    ticket_id INT PRIMARY KEY,
    price INT,
    time DATETIME,
    starting_stop_id INT NOT NULL,
    ending_stop_id INT NOT NULL,
    route_id INT NOT NULL,
    booking_type ENUM('online', 'offline'),
    FOREIGN KEY (starting_stop_id) REFERENCES Stops(Stop_id),
    FOREIGN KEY (ending_stop_id) REFERENCES Stops(Stop_id),
    FOREIGN KEY (route_id) REFERENCES Routes(Route_id)
);

CREATE TABLE Buses (
    Bus_id INT PRIMARY KEY,
    Status ENUM('active', 'inactive') default 'inactive',
    Bus_type_id INT,
    FOREIGN KEY (Bus_type_id) REFERENCES Bus_type(Bus_type_id)
);

CREATE TABLE Drivers (
    Driver_id INT PRIMARY KEY,
    name VARCHAR(50),
    Gender ENUM('male', 'female'),
    Salary INT
);
CREATE TABLE Conductors (
    conductor_id INT PRIMARY KEY,
    name VARCHAR(50),
    Gender ENUM('male', 'female'),
    Salary INT
);

CREATE TABLE Stops_in_route (
    node_id INT PRIMARY KEY,
    node_number_route INT default 0,
    Fair_stage INT default 0,
    Route_id INT,
    Stop_id_a INT,
    FOREIGN KEY (Route_id) REFERENCES Routes(Route_id),
    FOREIGN KEY (Stop_id_a) REFERENCES Stops(Stop_id)
);

CREATE TABLE Schedule (
    Schedule_id INT PRIMARY KEY,
    route ENUM('up', 'down') default 'up',
    time DATETIME,
    start_node_id INT,
    Bus_id INT,
    conductor_id INT,
    driver_id INT,
    FOREIGN KEY (start_node_id) REFERENCES Stops_in_route(node_id),
    FOREIGN KEY (Bus_id) REFERENCES Buses(Bus_id),
    FOREIGN KEY (conductor_id) REFERENCES Conductors(Conductor_id),
    FOREIGN KEY (driver_id) REFERENCES Drivers(Driver_id)
);

CREATE TABLE online_booked_ticket (
    booking_id INT PRIMARY KEY,
    time_of_booking DATETIME,
    user_id INT,
    ticket_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(User_id),
    FOREIGN KEY (ticket_id) REFERENCES Tickets(ticket_id)
);

INSERT INTO Bus_type (Bus_type_id, Capacity, Base_fare) VALUES
(1, 30, 10),
(2, 50, 5),
(3, 40, 10),
(4, 60, 10);

INSERT INTO Users (User_id, name, email, Gender, phone_number) VALUES
(1, 'Rahul Sharma', 'rahul.sharma@example.com', 'male', '9876543210'),
(2, 'Anita Desai', 'anita.desai@example.com', 'female', '8765432109'),
(3, 'Vikram Singh', 'vikram.singh@example.com', 'male', '7654321098'),
(4, 'Priya Verma', 'priya.verma@example.com', 'female', '6543210987');

INSERT INTO Stop_Location_Name (location_coordinate, location_name) VALUES
('28.6139,77.2090', 'Connaught Place'),  
('28.7041,77.1025', 'Rajiv Chowk'),      
('28.5355,77.3910', 'Dwarka Sector 21'), 
('28.6692,77.4538', 'Nehru Place'),      
('28.6082,77.2399', 'Khan Market'),      
('28.6128,77.2295', 'India Gate'),       
('28.5774,77.2418', 'Lajpat Nagar'),     
('28.5503,77.2078', 'Saket'),            
('28.5502,77.1272', 'Vasant Kunj'),      
('28.6469,77.2116', 'Karol Bagh');      



INSERT INTO Stops (Stop_id, Stop_Name, location_coordinate) VALUES
(1, 'Connaught Place', '28.6139,77.2090'),
(2, 'Rajiv Chowk', '28.7041,77.1025'),
(3, 'Dwarka Sector 21', '28.5355,77.3910'),
(4, 'Nehru Place', '28.6692,77.4538'),
(5, 'Khan Market', '28.6082,77.2399'),
(6, 'India Gate', '28.6128,77.2295'),
(7, 'Lajpat Nagar', '28.5774,77.2418'),
(8, 'Saket', '28.5503,77.2078'),
(9, 'Vasant Kunj', '28.5502,77.1272'),
(10, 'Karol Bagh', '28.6469,77.2116');



INSERT INTO Routes (Route_id, Bus_no, Avg_Duration, number_of_stops) VALUES
(1, 'DTC-123', '00:45:00', 6),
(2, 'DTC-456', '01:00:00', 10),
(3, 'DTC-789', '00:55:00', 8),
(4, 'DTC-321', '00:40:00', 5);

INSERT INTO Tickets (ticket_id, price, time, starting_stop_id, ending_stop_id, route_id, booking_type) VALUES
(1, 10, '2023-10-01 09:00:00', 1, 4, 1, 'online'),
(2, 15, '2023-10-01 09:15:00', 2, 5, 2, 'offline'),
(3, 12, '2023-10-01 09:30:00', 3, 6, 3, 'online'),
(4, 20, '2023-10-01 09:45:00', 4, 7, 4, 'offline');


INSERT INTO Buses (Bus_id, Status, Bus_type_id) VALUES
(1, 'active', 1),
(2, 'active', 2),
(3, 'inactive', 3),
(4, 'active', 4);


INSERT INTO Drivers (Driver_id, name, Gender, Salary) VALUES
(1, 'Ravi Kumar', 'male', 30000),
(2, 'Aditi Sharma', 'female', 35000),
(3, 'Suresh Yadav', 'male', 32000),
(4, 'Neha Singh', 'female', 33000);

INSERT INTO Conductors (conductor_id, name, Gender, Salary) VALUES
(1, 'Vinay Joshi', 'male', 25000),
(2, 'Sneha Kapoor', 'female', 27000),
(3, 'Ajay Mishra', 'male', 26000),
(4, 'Riya Verma', 'female', 28000);


INSERT INTO Stops_in_route (node_id, node_number_route, Fair_stage, Route_id, Stop_id_a) VALUES
(1, 1, 0, 1, 1),
(2, 2, 1, 1, 2),
(3, 3, 2, 1, 3),
(4, 4, 3, 1, 4),
(5, 5, 0, 2, 2),
(6, 6, 1, 2, 3),
(7, 7, 2, 2, 4),
(8, 8, 3, 2, 5),
(9, 9, 4, 3, 6),
(10, 10, 5, 3, 7),
(11, 11, 6, 3, 8);


INSERT INTO Schedule (Schedule_id, route, time, start_node_id, Bus_id, conductor_id, driver_id) VALUES
(1, 'up', '2023-10-01 08:00:00', 1, 1, 1, 1),
(2, 'down', '2023-10-01 08:30:00', 3, 2, 2, 2),
(3, 'up', '2023-10-01 09:00:00', 5, 3, 3, 3),
(4, 'down', '2023-10-01 09:30:00', 7, 4, 4, 4);


INSERT INTO online_booked_ticket (booking_id, time_of_booking, user_id, ticket_id) VALUES
(1, '2023-10-01 08:00:00', 1, 1),
(2, '2023-10-01 08:15:00', 2, 2),
(3, '2023-10-01 08:30:00', 3, 3),
(4, '2023-10-01 08:45:00', 4, 4);




show tables;
SELECT * FROM Bus_type;


SELECT * FROM Users;


SELECT * FROM Location_Name;

SELECT * FROM Stops;

SELECT * FROM Routes;


SELECT * FROM Tickets;


SELECT * FROM Buses;


SELECT * FROM Drivers;


SELECT * FROM Conductors;


SELECT * FROM Stops_in_route;


SELECT * FROM Schedule;


SELECT * FROM online_booked_ticket;


SELECT * FROM stop_Location_Name;



