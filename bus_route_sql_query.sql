DROP DATABASE Bus_Route;
CREATE DATABASE Bus_Route;
USE Bus_Route;
CREATE TABLE Bus_Type_Description (
    category VARCHAR(10) PRIMARY KEY,
    base_fare INT NOT NULL,
    discription TEXT
);

CREATE TABLE Bus_type (
    bus_type_id INT PRIMARY KEY,
    capacity INT,
    category VARCHAR(10),
    FOREIGN KEY (category) REFERENCES Bus_Type_Description(category)

    
);

CREATE TABLE Users (
    user_id INT PRIMARY KEY auto_increment,
    name VARCHAR(50),
    email VARCHAR(200),
    gender ENUM('male', 'female') default 'male',
    phone_number VARCHAR(12) NOT NULL,
    password  VARCHAR(500) NOt NULL
);
CREATE TABLE access_level(
	access_level_id int PRIMARY KEY,
    discription TEXT NOT NULL
);
CREATE TABLE Employee(
	emp_id INT PRIMARY KEY auto_increment,
    user_name VARCHAR(100),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    official_email VARCHAR(200) unique,
    account_password VARCHAR(50),
    phone_number VARCHAR(12) NOT NULL,
    access_level_id int NOT NULL,
    salary int,
    FOREIGN KEY(access_level_id) REFERENCES access_level(access_level_id)    
);
CREATE TABLE Stops (
    stop_id INT PRIMARY KEY,
    stop_name VARCHAR(50) NOT NULL unique,
    location_coordinate VARCHAR(50) NOT NULL
);


CREATE TABLE Routes (
    route_id INT PRIMARY KEY,
    bus_no VARCHAR(10) unique,
    avg_Duration TIME,
    number_of_stops INT NOT NULL
);


CREATE TABLE Buses (
    bus_id INT PRIMARY KEY,
    status ENUM('active', 'inactive') default 'inactive',
    bus_type_id INT,
    FOREIGN KEY (Bus_type_id) REFERENCES Bus_type(Bus_type_id) ON DELETE CASCADE
);



CREATE TABLE Staff (
    staff_id INT PRIMARY KEY,
    name VARCHAR(100),
    gender ENUM('male', 'female'),
    salary INT,
    role ENUM('driver', 'conductor') NOT NULL
);

/*
CREATE TABLE Drivers (
    Driver_id INT PRIMARY KEY,
    Staff_id INT,
    FOREIGN KEY (Staff_id) REFERENCES Staff(Staff_id) ON DELETE CASCADE

);
CREATE TABLE Conductors (
    Conductor_id INT PRIMARY KEY,
    Staff_id INT,
    FOREIGN KEY (Staff_id) REFERENCES Staff(Staff_id) ON DELETE CASCADE

);
*/



CREATE TABLE Stops_in_route (
    node_id INT PRIMARY KEY,
    route_stop_number INT,
    Fare_stage INT default 1,
    Route_id INT NOT NULL,
    stop_id INT NOT NULL,
    FOREIGN KEY (Route_id) REFERENCES Routes(Route_id) ON DELETE CASCADE,
    FOREIGN KEY (Stop_id) REFERENCES Stops(Stop_id) ON DELETE RESTRICT,
    unique(Route_id, Stop_id, route_stop_number)
);
CREATE TABLE Tickets (
    ticket_id INT PRIMARY KEY,
    price INT NOT NULL,
    route ENUM('up', 'down'),
    gender ENUM('Male', 'Female'),
    date_of_tickets date,
    category varchar(10),
    ticket_type ENUM('online', 'offline') NOT NULL,
	FOREIGN KEY (category) REFERENCES Bus_Type_Description(category)
);


CREATE TABLE Offline_Tickets (
    offline_ticket_id INT PRIMARY KEY,
    ticket_id INT,
    route_id INT NOT NULL,
    FOREIGN KEY (ticket_id) REFERENCES Tickets(ticket_id) ON DELETE CASCADE,
	FOREIGN KEY (route_id) REFERENCES Routes(route_id) ON DELETE CASCADE
);


CREATE TABLE Online_Tickets (
    online_ticket_id INT PRIMARY KEY,
    ticket_id INT,
    time_of_booking TIME,
    starting_node_id INT NOT NULL,
    ending_node_id INT NOT NULL,
    user_id INT,
    FOREIGN KEY (Ticket_id) REFERENCES Tickets(Ticket_id) ON DELETE CASCADE,
    FOREIGN KEY (starting_node_id) REFERENCES Stops_in_route(node_id) ON DELETE RESTRICT,
    FOREIGN KEY (ending_node_id) REFERENCES Stops_in_route(node_id) ON DELETE RESTRICT,
    FOREIGN KEY (user_id) REFERENCES Users(User_id) ON DELETE CASCADE

);
CREATE TABLE Schedule (
    schedule_id INT PRIMARY KEY,
    schedule_date Date,
    route ENUM('up', 'down') default 'up',
	time time,
    route_id int NOT NULL,
    start_node_number INT NOT NULL,
    stop_node_number INT NOT NULL,
    bus_id INT,
    conductor_id INT,
    driver_id INT,
    FOREIGN KEY (route_id) REFERENCES Routes(route_id) ON DELETE RESTRICT,
    FOREIGN KEY (Bus_id) REFERENCES Buses(Bus_id) ON DELETE RESTRICT,
    FOREIGN KEY (conductor_id) REFERENCES Staff(staff_id) ON DELETE RESTRICT,
    FOREIGN KEY (driver_id) REFERENCES Staff(staff_id) ON DELETE RESTRICT
);
CREATE TABLE bus_stop_reach_time(
    reach_time_id INT PRIMARY KEY auto_increment,
    route ENUM('up', 'down') default 'up',
	time time,
    node_number INT NOT NULL,
    schedule_id int,
    unique (node_number, schedule_id),
    FOREIGN KEY (schedule_id) REFERENCES schedule(schedule_id) ON DELETE CASCADE
);
INSERT INTO Access_level(access_level_id, discription) VALUES 
(1,'edit data'),
(2, 'update data'),
(3, 'only View');
INSERT INTO Employee(first_name, last_name, User_name, salary, official_email, account_password, phone_number, access_level_id) VALUE
('Ashutosh', 'Ranjan', 'Ashutosh_ranjan_DBA', 100000,'ashu@gmail.com', '@819', '1234567891', 1),
('Pankaj', '', 'Pankaj_DBA', 80000,'pankaj@gmail.com', '@1234', '9868952481', 2);
INSERT INTO Bus_Type_Description (category, Base_fare, Discription) VALUES
('blue',10, 'AC'),
('red',10, 'AC'),
('green',5, 'NON_AC'),
('orange',5, 'NON_AC');

INSERT INTO Bus_type (Bus_type_id, Capacity, category) VALUES
(1, 40, 'red'),
(2, 50, 'green'),
(3, 40, 'red'),
(4, 50, 'orange');
INSERT INTO Users (name, email, Gender, phone_number, password) VALUES
('Rahul Sharma', 'rahul.sharma@example.com', 'male', '9876543210',"passwordhash1"),
('Anita Desai', 'anita.desai@example.com', 'female', '8765432109',"passwordhash2"),
('Vikram Singh', 'vikram.singh@example.com', 'male', '7654321098',"passwordhash3"),
('Priya Verma', 'priya.verma@example.com', 'female', '6543210987',"passwordhash4");
   



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

INSERT INTO Routes (Route_id, Bus_no, Avg_Duration, number_of_stops) VALUES
(4, 'DTC-145','2:00:00',7);


INSERT INTO Buses (Bus_id, Status, Bus_type_id) VALUES
(1, 'active', 1),
(2, 'active', 2),
(3, 'inactive', 3),
(4, 'active', 4);

INSERT INTO Staff (staff_id, name, Gender, Salary, Role) VALUES
(1, 'Ravi', 'male', 30000, 'Driver'),
(2, 'Aditi', 'female', 29000, 'Driver'),
(3, 'Suresh', 'male', 32000, 'Driver'),
(4, 'Vinay', 'male', 25000, 'Conductor'),
(5, 'Sneha', 'female', 17000, 'Conductor'),
(6, 'Ajay', 'male', 26000, 'Conductor');
/*
INSERT INTO Drivers (Driver_id, staff_id) VALUES
(1, 1),
(2, 2),
(3, 3);

INSERT INTO Conductors (conductor_id, staff_id) VALUES
(1, 4),
(2, 5),
(3, 6);
*/

INSERT INTO Stops_in_route (node_id, Stop_id, Fare_stage, Route_id, route_stop_number) VALUES
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

INSERT INTO Schedule (Schedule_id, Schedule_date, route, time, route_id, start_node_number, stop_node_number, Bus_id, conductor_id, driver_id) VALUES
(1, '2024-10-06', 'up', '08:00:00', 1, 3, 6, 1, 4, 3),
(2, '2024-10-06', 'down', '10:30:00', 1, 6, 3, 1, 4, 3),
(3, '2024-10-06', 'up', '16:00:00', 1, 1, 6, 1, 4, 3),
(4, '2024-10-06', 'down', '18:00:00', 1, 6, 1, 1, 4, 3),
(5, '2024-10-06', 'up', '09:00:00', 2, 1, 3, 2, 5, 2),
(6, '2024-10-06', 'down', '10:00:00', 2, 3, 1, 2, 5, 2),
(7, '2024-10-06', 'up', '12:00:00', 3, 1, 3, 3, 6, 1),
(8, '2024-10-06', 'down', '13:45:00', 3, 3, 1, 3, 6, 1);


INSERT INTO bus_stop_reach_time (route, time, node_number, schedule_id) 
VALUES 
('up', '8:1:00', 3, 1),
('up', '8:1:00', 4, 1),
('up', '8:3:00', 5, 1),
('up', '8:8:00', 6, 1),
('up', '16:5:00', 1, 3),
('up', '16:5:00', 2, 3),
('up', '16:5:00', 3, 3),
('up', '16:9:00', 4, 3),
('up', '16:11:00', 5, 3),
('up', '16:16:00', 6, 3),
('up', '9:3:00', 1, 5),
('up', '9:10:00', 2, 5),
('up', '9:16:00', 3, 5),
('up', '12:7:00', 1, 7),
('up', '12:11:00', 2, 7),
('up', '12:14:00', 3, 7),
('down', '10:35:00', 6, 2),
('down', '10:40:00', 5, 2),
('down', '10:47:00', 4, 2),
('down', '10:51:00', 3, 2),
('down', '18:33:00', 6, 4),
('down', '18:38:00', 5, 4),
('down', '18:43:00', 4, 4),
('down', '18:51:00', 3, 4),
('down', '18:55:00', 2, 4),
('down', '18:59:00', 1, 4),
('down', '10:8:00', 3, 6),
('down', '10:15:00',2, 6),
('down', '10:20:00', 1, 6),
('down', '13:50:00', 3, 8),
('down', '13:54:00', 2, 8),
('down', '13:58:00', 1, 8);

select * from schedule join buses on schedule.bus_id = buses.bus_id join bus_type on bus_type.bus_type_id = buses.bus_type_id;
INSERT INTO Tickets (Ticket_id, price, route, gender, ticket_type, Date_of_tickets, category) VALUES
(1, 20, 'up', 'Male', 'offline','2024-10-06', 'red'),
(2, 15, 'up', 'Male', 'offline','2024-10-06', 'green'),
(3, 15, 'up', 'Female', 'offline','2024-10-06',  'red'),
(4, 20, 'up', 'Female', 'offline','2024-10-06',  'red'),
(5, 20, 'down', 'Male', 'offline','2024-10-06', 'red'),
(6, 20, 'down', 'Male', 'offline','2024-10-06', 'red'),
(7, 25, 'up', 'Female', 'offline','2024-10-06', 'red'),
(8, 10, 'up', 'Male', 'offline','2024-10-06', 'green'),
(9, 15, 'down', 'Male', 'offline','2024-10-06', 'red'),
(10, 15, 'down', 'Male', 'offline','2024-10-06', 'green'),
(11, 20, 'up', 'Female', 'offline','2024-10-06', 'red'),
(12, 25, 'up', 'Male', 'offline','2024-10-06', 'red'),
(13, 15, 'down', 'Female', 'offline','2024-10-06', 'green'),
(14, 25, 'down', 'Male', 'offline','2024-10-06', 'red'),
(15, 15, 'up', 'Male', 'offline','2024-10-06', 'green'),
(16, 15, 'up', 'Female', 'offline','2024-10-06', 'green'),
(17, 25, 'down', 'Female', 'offline','2024-10-06', 'red'),
(18, 25, 'up', 'Male', 'offline','2024-10-06', 'red'),
(19, 25, 'down', 'Male', 'offline','2024-10-06', 'red'),
(20, 15, 'down', 'Female', 'offline','2024-10-06', 'green'),
(21, 20, 'up', 'Male', 'online','2024-10-06', 'red'),
(22, 15, 'up', 'Female', 'online','2024-10-06', 'green'),
(23, 20, 'up', 'Female', 'online','2024-10-06', 'red'),
(24, 25, 'up', 'Female', 'online','2024-10-06', 'red'),
(25, 15, 'up', 'Male', 'online','2024-10-06', 'green'),
(26, 20, 'up', 'Female', 'online','2024-10-06', 'red'),
(27, 15, 'up', 'Male', 'online','2024-10-06', 'green'),
(28, 15, 'up', 'Male', 'online','2024-10-06', 'green'),
(29, 25, 'up', 'Female', 'online','2024-10-06', 'red'),
(30, 25, 'up', 'Female', 'online','2024-10-06', 'red');

INSERT INTO Offline_Tickets (Offline_ticket_id, Ticket_id, route_id) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 1),
(5, 5, 2),
(6, 6, 3),
(7, 7, 1),
(8, 8, 2),
(9, 9, 1),
(10, 10, 2),
(11, 11, 1),
(12, 12, 3),
(13, 13, 1),
(14, 14, 2),
(15, 15, 2),
(16, 16, 3),
(17, 17, 1),
(18, 18, 2),
(19, 19, 1),
(20, 20, 3);

INSERT INTO Online_Tickets (Online_ticket_id, Ticket_id, time_of_booking, starting_node_id, ending_node_id, user_id) VALUES
(1, 21, '08:00:00', 1, 6, 1),
(2, 22, '09:00:00', 12, 16, 3),
(3, 23, '10:30:00', 9, 7, 4),
(4, 24, '12:00:00', 1, 4, 2),
(5, 25, '13:30:00', 3, 6, 1),
(6, 26, '15:00:00', 4, 6, 2),
(7, 27, '16:30:00', 1, 6, 3),
(8, 28, '17:45:00', 3, 9, 4),
(9, 29, '18:30:00', 2, 5, 1),
(10, 30, '20:00:00', 1, 6, 2);


 





show tables;
SELECT * FROM Bus_type;
SELECT * FROM Users;
SELECT * FROM Access_level;
SElECT * FROM Employee;
SELECT * FROM Stops;
SELECT * FROM Routes;
SELECT * FROM Buses;
select * from Staff;
/*
SELECT * FROM Drivers;
SELECT * FROM Conductors;
*/
SELECT * FROM Stops_in_route;
SELECT * FROM Schedule;
select * from Tickets;
SELECT * FROM Online_tickets;
SELECT * FROM Offline_tickets;
SELECT * FROM bus_stop_reach_time;


-- all stop connectivity
select Routes.Route_id,bus_no ,node_id, route_stop_number, fare_stage, stops_In_route.stop_id, stop_Name, location_coordinate
from Stops_In_Route
join Stops on Stops.stop_id = Stops_In_Route.stop_id
join Routes on Routes.route_id = Stops_In_Route.route_id
order by Route_id, route_stop_number;


-- stop by bus number
select * from 
Stops_In_Route sir
join Stops on Stops.stop_id = sir.stop_id
join routes rt on sir.route_id = rt.route_id
where rt.bus_no like '%123'
order by route_stop_number;


select * from 
Stops_In_Route sir
join Stops on Stops.stop_id = sir.stop_id
join routes rt on sir.route_id = rt.route_id
order by rt.route_id, route_stop_number;


-- driver and Conductor  name for each schedule 
select Schedule_id, route, Time, start_node_number, stop_node_number, Bus_id, sch.driver_id, Stfd.name
driver_name, stfd.Gender, stfd.Salary, sch.conductor_id , stfc.name conductor_name, stfc.Gender, stfc.Salary
from schedule sch
join Staff stfc ON stfc.staff_id = sch.driver_id
join Staff stfd ON stfd.staff_id = sch.conductor_id 
order by schedule_id;

-- number of tickets and total fair
select  count(*) total_number_of_tickets,sum(price) total_fair, tk.ticket_type from
tickets tk
group by tk.ticket_type;

-- online tickets booked for each stops
select  count(*) total__online_tickets,sum(price) total__online_fair, st.stop_id, st.stop_name
from online_tickets ont
join stops_in_route sir on sir.node_id = ont.ending_node_id
join stops st on sir.stop_id = st.stop_id 
join tickets tk ON tk.ticket_id = ont.ticket_id
group by st.stop_id;


-- all bus stop reach times with stop name
SELECT sch.route_id, rt.bus_no, brt.route, sch.schedule_date , brt.time, brt.node_number, brt.schedule_id,
 st.Stop_Name, st.location_coordinate
FROM bus_stop_reach_time brt
JOIN schedule sch ON brt.schedule_id = sch.Schedule_id
JOIN stops_in_route sir ON brt.node_number = sir.route_stop_number and sch.route_id = sir.route_id
JOIN stops st ON sir.Stop_id = st.Stop_id
JOIN routes rt ON sch.route_id = rt.route_id
ORDER BY sch.schedule_date, sch.route_id, sch.schedule_id, brt.time;

-- first and last bus time on each stop
SELECT st.stop_name, MIN(bsrt.time) first_bus_time, MAX(bsrt.time) last_bus_time
FROM bus_stop_reach_time bsrt
JOIN stops_in_route sir ON bsrt.node_number = sir.route_stop_number
JOIN stops st ON sir.stop_id = st.stop_id
GROUP BY st.stop_name
ORDER BY st.stop_name;


select * from 
Stops_In_Route sir
join Stops_In_Route sir2 on sir.stop_id = sir2.stop_id and sir.route_id != sir2.route_id
order by sir.route_id;


select * from routes;


select sir.*, sir2.route_id other_route_id, sir2.route_stop_number other_route_stop_number from 
Stops_In_Route sir
join Stops_In_Route sir2 on sir.stop_id = sir2.stop_id;