
INSERT INTO Access_level(access_level_id, discription) VALUES 
(1,'edit data'),
(2, 'update data'),
(3, 'only View');
INSERT INTO Employee(first_name, last_name, User_name, salary, official_email, password, phone_number, access_level_id) VALUE
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

INSERT INTO Schedule (Schedule_id, route, time, route_id, start_stop_number, stop_stop_number, Bus_id, conductor_id, driver_id, schedule_day) VALUES
(1, 'up', '08:00:00', 1, 3, 6, 1, 4, 3, 'monday'),
(2, 'down', '10:30:00', 1, 6, 3, 1, 4, 3, 'monday'),
(3, 'up', '16:00:00', 1, 1, 6, 1, 4, 3, 'monday'),
(4, 'down', '18:00:00', 1, 6, 1, 1, 4, 3, 'monday'),
(5, 'up', '09:00:00', 2, 1, 3, 2, 5, 2, 'monday'),
(6, 'down', '10:00:00', 2, 3, 1, 2, 5, 2, 'monday'),
(7, 'up', '12:00:00', 3, 1, 3, 3, 6, 1, 'monday'),
(8, 'down', '13:45:00', 3, 3, 1, 3, 6, 1, 'monday');


INSERT INTO bus_stop_reach_time (time, node_number, schedule_id) 
VALUES 
('8:1:00', 3, 1),
('8:1:00', 4, 1),
('8:3:00', 5, 1),
('8:8:00', 6, 1),
( '16:5:00', 1, 3),
( '16:5:00', 2, 3),
( '16:5:00', 3, 3),
( '16:9:00', 4, 3),
( '16:11:00', 5, 3),
( '16:16:00', 6, 3),
( '9:3:00', 1, 5),
( '9:10:00', 2, 5),
( '9:16:00', 3, 5),
( '12:7:00', 1, 7),
( '12:11:00', 2, 7),
( '12:14:00', 3, 7),
( '10:35:00', 6, 2),
( '10:40:00', 5, 2),
( '10:47:00', 4, 2),
( '10:51:00', 3, 2),
( '18:33:00', 6, 4),
( '18:38:00', 5, 4),
( '18:43:00', 4, 4),
( '18:51:00', 3, 4),
( '18:55:00', 2, 4),
( '18:59:00', 1, 4),
( '10:8:00', 3, 6),
( '10:15:00',2, 6),
( '10:20:00', 1, 6),
( '13:50:00', 3, 8),
( '13:54:00', 2, 8),
( '13:58:00', 1, 8);


INSERT INTO Tickets (price, route_id, gender, ticket_type, date_of_tickets, category) VALUES
(20, 1, 'Male', 'offline', '2024-10-06', 'red'),
(15, 2, 'Male', 'offline', '2024-10-06', 'green'),
(15, 1, 'Female', 'offline', '2024-10-06', 'red'),
(20, 2, 'Female', 'offline', '2024-10-06', 'red'),
(20, 3, 'Male', 'offline', '2024-10-06', 'red'),
(20, 2, 'Male', 'offline', '2024-10-06', 'red'),
(25, 1, 'Female', 'offline', '2024-10-06', 'red'),
(10, 2, 'Male', 'offline', '2024-10-06', 'green'),
(15, 3, 'Male', 'offline', '2024-10-06', 'red'),
(15, 1, 'Male', 'offline', '2024-10-06', 'green'),
(20, 2, 'Female', 'offline', '2024-10-06', 'red'),
(25, 3, 'Male', 'offline', '2024-10-06', 'red'),
(15, 2, 'Female', 'offline', '2024-10-06', 'green'),
(25, 1, 'Male', 'offline', '2024-10-06', 'red'),
(15, 3, 'Male', 'offline', '2024-10-06', 'green'),
(15, 2, 'Female', 'offline', '2024-10-06', 'green'),
(25, 3, 'Female', 'offline', '2024-10-06', 'red'),
(25, 1, 'Male', 'offline', '2024-10-06', 'red'),
(25, 2, 'Male', 'offline', '2024-10-06', 'red'),
(15, 3, 'Female', 'offline', '2024-10-06', 'green'),
(20, 1, 'Male', 'online', '2024-10-06', 'red'),
(15, 2, 'Female', 'online', '2024-10-06', 'green'),
(20, 1, 'Female', 'online', '2024-10-06', 'red'),
(25, 3, 'Female', 'online', '2024-10-06', 'red'),
(15, 1, 'Male', 'online', '2024-10-06', 'green'),
(20, 2, 'Female', 'online', '2024-10-06', 'red'),
(15, 3, 'Male', 'online', '2024-10-06', 'green'),
(15, 1, 'Male', 'online', '2024-10-06', 'green'),
(25, 2, 'Female', 'online', '2024-10-06', 'red'),
(25, 1, 'Female', 'online', '2024-10-06', 'red');


INSERT INTO Offline_Tickets (ticket_id, direction) VALUES
(1, 'up'),
(2, 'up'),
(3, 'up'),
(4, 'down'),
(5, 'up'),
(6, 'down'),
(7, 'up'),
(8, 'up'),
(9, 'down'),
(10, 'down'),
(11, 'up'),
(12, 'up'),
(13, 'down'),
(14, 'down'),
(15, 'up'),
(16, 'up'),
(17, 'down'),
(18, 'up'),
(19, 'down'),
(20, 'down');


INSERT INTO Online_Tickets (ticket_id, time_of_booking, starting_stop_number, ending_stop_number, user_id) VALUES
(21, '08:00:00', 1, 6, 1),
(22, '09:00:00', 12, 16, 3),
(23, '10:30:00', 9, 7, 4),
(24, '12:00:00', 1, 4, 2),
(25, '13:30:00', 3, 6, 1),
(26, '15:00:00', 4, 6, 2),
(27, '16:30:00', 1, 6, 3),
(28, '17:45:00', 3, 9, 4),
(29, '18:30:00', 2, 5, 1),
(30, '20:00:00', 1, 6, 2);
