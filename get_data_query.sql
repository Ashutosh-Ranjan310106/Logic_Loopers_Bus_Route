use bus_route;

USE Bus_Route;
show tables;

SELECT * from emp_session;
desc employee;
SELECT * FROM Bus_type;
SELECT * FROM Users;
SELECT * FROM User_log;
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
select Schedule_id, route, Time, start_stop_number, stop_stop_number, Bus_id, sch.driver_id, Stfd.name
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
join stops_in_route sir on sir.node_id = ont.ending_stop_number
join stops st on sir.stop_id = st.stop_id 
join tickets tk ON tk.ticket_id = ont.ticket_id
group by st.stop_id;
use Bus_Route;
-- all bus stop reach times with stop name
SELECT  stop_name, bsrt.time bus_time, bus_no, st.stop_id, sch.route direction
FROM bus_stop_reach_time bsrt
JOIN schedule sch ON sch.schedule_id = bsrt.schedule_id
JOIN stops_in_route sir ON  bsrt.node_number = sir.route_stop_number and sch.route_id = sir.route_id
JOIN routes rt ON rt.route_id = sch.route_id
JOIN stops st ON sir.stop_id = st.stop_id
ORDER BY bsrt.time;

-- first and last bus time on each stop
SELECT st.stop_name, MIN(bsrt.time) first_bus_time, MAX(bsrt.time) last_bus_time
FROM bus_stop_reach_time bsrt
JOIN stops_in_route sir ON bsrt.node_number = sir.route_stop_number
JOIN stops st ON sir.stop_id = st.stop_id
GROUP BY st.stop_name
ORDER BY st.stop_name;

