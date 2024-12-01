DROP DATABASE Bus_Route;
CREATE DATABASE Bus_Route;
USE Bus_Route;
SET SQL_SAFE_UPDATES = 0;

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
    email VARCHAR(200) not null unique,
    gender ENUM('Male', 'Female', 'Other') default 'Male',
    phone_number VARCHAR(12)  not null unique,
    password  VARCHAR(500) NOt NULL
);

CREATE TABLE User_log (
	user_log_id int PRIMARY KEY auto_increment,
    user_ip varchar(50) NOT NULL,
    user_id int NOT NULL,
    status int default 1,
    login_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
CREATE TABLE access_level(
	access_level_id int PRIMARY KEY,
    discription TEXT NOT NULL
);
CREATE TABLE Employee(
	emp_id INT PRIMARY KEY auto_increment,
    user_name VARCHAR(100) unique,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    official_email VARCHAR(200) unique,
    password VARCHAR(200),
    phone_number VARCHAR(12) NOT NULL unique,
    access_level_id int NOT NULL,
    salary int,
    gender ENUM('Male', 'Female', 'Other') default 'Male',
    FOREIGN KEY(access_level_id) REFERENCES access_level(access_level_id)    
);
CREATE TABLE Emp_session(
	Session_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_ip varchar(50) NOT NULL,
    emp_id INT NOT NULL,
    status bool DEFAULT 1,
	session_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(emp_id) REFERENCES Employee(emp_id)
);
CREATE TABLE Stops (
    stop_id INT PRIMARY KEY auto_increment,
    stop_name VARCHAR(200) NOT NULL unique,
    location_coordinate VARCHAR(100)
);

CREATE INDEX idx_stop_name ON stops(stop_name);


CREATE TABLE Routes (
    route_id INT PRIMARY KEY AUTO_INCREMENT,
    bus_no VARCHAR(10) unique,
    avg_Duration TIME,
    number_of_stops INT NOT NULL,
    total_number_of_trip INT
);
alter table Routes add number_of_stops INT NOT NULL;

CREATE TABLE Buses (
    bus_id INT PRIMARY KEY AUTO_INCREMENT,
    status ENUM('active', 'inactive') default 'inactive',
    bus_type_id INT,
    FOREIGN KEY (Bus_type_id) REFERENCES Bus_type(Bus_type_id) ON DELETE CASCADE
);



CREATE TABLE Staff (
    staff_id INT PRIMARY KEY AUTO_INCREMENT,
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
    node_id INT PRIMARY KEY AUTO_INCREMENT,
    route_stop_number INT,
    Fare_stage INT default 1,
    Route_id INT NOT NULL,
    stop_id INT NOT NULL,
    FOREIGN KEY (Route_id) REFERENCES Routes(Route_id) ON DELETE CASCADE,
    FOREIGN KEY (Stop_id) REFERENCES Stops(Stop_id) ON DELETE RESTRICT,
    unique(Route_id, Stop_id, route_stop_number)
);
CREATE TABLE Tickets (
    ticket_id INT PRIMARY KEY AUTO_INCREMENT,
    price INT NOT NULL,
	route_id INT NOT NULL,
    gender ENUM('Male', 'Female'),
    date_of_tickets date ,
    category varchar(10),
    ticket_type ENUM('online', 'offline') NOT NULL,
	FOREIGN KEY (category) REFERENCES Bus_Type_Description(category),
	FOREIGN KEY (route_id) REFERENCES Routes(route_id) ON DELETE CASCADE
);



CREATE TABLE Offline_tickets (
    offline_ticket_id INT PRIMARY KEY AUTO_INCREMENT,
    ticket_id INT,
	direction ENUM('up', 'down'),
    FOREIGN KEY (ticket_id) REFERENCES Tickets(ticket_id) ON DELETE CASCADE

);


CREATE TABLE Online_Tickets (
    online_ticket_id INT PRIMARY KEY AUTO_INCREMENT,
    ticket_id INT,
    time_of_booking TIME,
    starting_stop_number INT NOT NULL,
    ending_stop_number INT NOT NULL,
    user_id INT,
    FOREIGN KEY (Ticket_id) REFERENCES Tickets(Ticket_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES Users(User_id) ON DELETE CASCADE

);
CREATE TABLE Schedule (
    schedule_id INT PRIMARY KEY AUTO_INCREMENT,
    schedule_day ENUM('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'firday', 'saturday'),
    route ENUM('up', 'down') default 'up',
	time time,
    route_id int NOT NULL,
    start_stop_number INT NOT NULL,
    stop_stop_number INT NOT NULL,
    bus_id INT,
    conductor_id INT,
    driver_id INT,
    FOREIGN KEY (route_id) REFERENCES Routes(route_id) ON DELETE CASCADE,
    FOREIGN KEY (Bus_id) REFERENCES Buses(Bus_id) ON DELETE RESTRICT,
    FOREIGN KEY (conductor_id) REFERENCES Staff(staff_id) ON DELETE RESTRICT,
    FOREIGN KEY (driver_id) REFERENCES Staff(staff_id) ON DELETE RESTRICT
);
CREATE TABLE bus_stop_reach_time(
    reach_time_id INT PRIMARY KEY AUTO_INCREMENT,
	time time,
    node_number INT NOT NULL,
    schedule_id int,
    unique (node_number, schedule_id),
    FOREIGN KEY (schedule_id) REFERENCES schedule(schedule_id) ON DELETE CASCADE
);
 
            
