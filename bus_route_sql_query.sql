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
CREATE TABLE Stops (
    Stop_id INT PRIMARY KEY,
    Stop_Name VARCHAR(50) NOT NULL unique,
    location_coordinate VARCHAR(50) NOT NULL
);


CREATE TABLE Routes (
    Route_id INT PRIMARY KEY,
    Bus_no VARCHAR(10) unique,
    Avg_Duration TIME,
    number_of_stops INT NOT NULL
);

CREATE TABLE Tickets (
    ticket_id INT PRIMARY KEY,
    price INT,
    time DATETIME,
    starting_stop_id INT NOT NULL,
    ending_stop_id INT NOT NULL,
    route_id INT NOT NULL,
    booking_type ENUM('online', 'offline'),
    FOREIGN KEY (starting_stop_id) REFERENCES Stops(Stop_id) ON DELETE RESTRICT,
    FOREIGN KEY (ending_stop_id) REFERENCES Stops(Stop_id) ON DELETE RESTRICT,
    FOREIGN KEY (route_id) REFERENCES Routes(Route_id) ON DELETE RESTRICT
);

CREATE TABLE Buses (
    Bus_id INT PRIMARY KEY,
    Status ENUM('active', 'inactive') default 'inactive',
    Bus_type_id INT,
    FOREIGN KEY (Bus_type_id) REFERENCES Bus_type(Bus_type_id) ON DELETE CASCADE
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
    route_node_number INT,
    Fair_stage INT default 1,
    Route_id INT NOT NULL,
    Stop_id INT NOT NULL,
    FOREIGN KEY (Route_id) REFERENCES Routes(Route_id) ON DELETE CASCADE,
    FOREIGN KEY (Stop_id) REFERENCES Stops(Stop_id) ON DELETE RESTRICT
);

CREATE TABLE Schedule (
    Schedule_id INT PRIMARY KEY,
    route ENUM('up', 'down') default 'up',
	Time time,
    start_node_id INT NOT NULL,
    stop_node_id INT NOT NULL,
    Bus_id INT,
    conductor_id INT,
    driver_id INT,
    FOREIGN KEY (start_node_id) REFERENCES Stops_in_route(node_id) ON DELETE RESTRICT,
    FOREIGN KEY (stop_node_id) REFERENCES Stops_in_route(node_id) ON DELETE RESTRICT,
    FOREIGN KEY (Bus_id) REFERENCES Buses(Bus_id) ON DELETE RESTRICT,
    FOREIGN KEY (conductor_id) REFERENCES Conductors(Conductor_id) ON DELETE RESTRICT,
    FOREIGN KEY (driver_id) REFERENCES Drivers(Driver_id) ON DELETE RESTRICT
);

CREATE TABLE online_booked_ticket (
    booking_id INT PRIMARY KEY,
    time_of_booking DATETIME,
    user_id INT,
    ticket_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(User_id) ON DELETE CASCADE,
    FOREIGN KEY (ticket_id) REFERENCES Tickets(ticket_id) ON DELETE CASCADE
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
   



INSERT INTO Stops (Stop_id, Stop_Name, location_coordinate) VALUES
(1, 'a', '28.6139,77.2090'),
(2, 'b', '28.7041,77.1025'),
(3, 'c', '28.5355,77.3910'),
(4, 'd', '28.6692,77.4538'),
(5, 'e', '28.6082,77.2399'),
(6, 'f', '28.6128,77.2295'),
(7, 'g', '28.5774,77.2418'),
(8, 'h', '28.5503,77.2078'),
(9, 'i', '28.5502,77.1272'),
(10, 'j', '28.6469,77.2116'),
(11, 'k', '02.6469,03.2116');



INSERT INTO Routes (Route_id, Bus_no, Avg_Duration, number_of_stops) VALUES
(1, 'DTC-123', '01:00:00', 6),
(2, 'DTC-456', '00:45:00', 5),
(3, 'DTC-789', '00:55:00', 5);
/*
INSERT INTO Tickets (ticket_id, price, time, starting_stop_id, ending_stop_id, route_id, booking_type) VALUES
(1, 10, '2023-10-01 09:00:00', 1, 4, 1, 'online'),
(2, 15, '2023-10-01 09:15:00', 2, 5, 2, 'offline'),
(3, 12, '2023-10-01 09:30:00', 3, 6, 3, 'online'),
(4, 20, '2023-10-01 09:45:00', 4, 7, 4, 'offline');
*/

INSERT INTO Buses (Bus_id, Status, Bus_type_id) VALUES
(1, 'active', 1),
(2, 'active', 2),
(3, 'inactive', 3),
(4, 'active', 4);


INSERT INTO Drivers (Driver_id, name, Gender, Salary) VALUES
(1, 'Ravi', 'male', 30000),
(2, 'Aditi', 'female', 25000),
(3, 'Suresh', 'male', 32000);

INSERT INTO Conductors (conductor_id, name, Gender, Salary) VALUES
(1, 'Vinay', 'male', 25000),
(2, 'Sneha', 'female', 17000),
(3, 'Ajay', 'male', 26000);


INSERT INTO Stops_in_route (node_id, Stop_id, Fair_stage, Route_id, route_node_number) VALUES
(1, 1, 1, 1, 1),
(2, 2, 2, 1, 2),
(3, 3, 2, 1, 3),
(4, 4, 3, 1, 4),
(5, 5, 3, 1, 5),
(6, 6, 4, 1, 6),
(7, 4, 1, 2, 1),
(8, 9, 1, 2, 2),
(9, 10, 2, 2, 3),
(10, 8, 2, 2, 4),
(11, 7, 2, 2, 5),
(12, 3, 1, 3, 1),
(13, 9, 1, 3, 2),
(14, 11, 2, 3, 3),
(15, 7, 3, 3, 4),
(16, 6, 3, 3, 5);


INSERT INTO Schedule (Schedule_id, route, time, start_node_id, stop_node_id, Bus_id, conductor_id, driver_id) VALUES
(1, 'up', '08:00:00', 3, 6, 1, 1, 3),
(2, 'down', '10:30:00', 6, 3, 1, 1, 3),
(3, 'up', '04:00:00', 1, 6, 1, 1, 3),
(4, 'down', '06:00:00', 6, 1, 1, 1, 3),
(5, 'up', '09:00:00', 7, 9, 2, 2, 2),
(6, 'down', '10:00:00', 9, 7, 2, 2, 2),
(7, 'up', '12:00:00', 12, 14, 3, 3, 1),
(8, 'down', '01:45:00', 12, 14, 3, 3, 1);


INSERT INTO online_booked_ticket (booking_id, time_of_booking, user_id, ticket_id) VALUES
(1, '2023-10-01 08:00:00', 1, 1),
(2, '2023-10-01 08:15:00', 2, 2),
(3, '2023-10-01 08:30:00', 3, 3),
(4, '2023-10-01 08:45:00', 4, 4);




 





show tables;
SELECT * FROM Bus_type;
SELECT * FROM Users;
SELECT * FROM Stop_Location_Name;
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


-- all stop conectivity
select node_id, route_node_number, Fair_stage, Route_id, Stops_In_Route.Stop_id, Stop_Name, location_coordinate from Stops_In_Route
join Stops on Stops.stop_id = Stops_In_Route.stop_id
order by Route_id;


-- schdule for particular route
select Schedule_id, route, Time, start_node_id, stop_node_id, Bus_id, conductor_id, driver_id, route_node_number, Fair_stage, rt.Route_id, Bus_no, Avg_Duration, number_of_stops
from schedule sch
join stops_in_route sir on sch.start_node_id = sir.node_id
join routes rt on sir.route_id = rt.route_id
where rt.route_id = 3;

-- stop by bus number
select *
from Stops_In_Route sir
join Stops on Stops.stop_id = sir.stop_id
join routes rt on sir.route_id = rt.route_id
where rt.bus_no like '%456'
order by route_node_number;

-- driver and Conductor  name for each schedule 
select Schedule_id, route, Time, start_node_id, stop_node_id, Bus_id, dri.Driver_id, dri.name driver_name, dri.Gender, dri.Salary, cdr.conductor_id, cdr.name conductor_name, cdr.Gender, cdr.Salary
from schedule sch
join Drivers dri on dri.driver_id = sch.driver_id
join Conductors cdr on cdr.conductor_id = sch.conductor_id
order by schedule_id;



