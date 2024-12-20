from flask import render_template, jsonify

class View:
    @staticmethod
    def render_success(message, emp_id=None):
        r =  {
            "status": "success",
            "message": message,
        }
        if emp_id:
            r["id"] = emp_id
        return r
    @staticmethod
    def render_fare(fare, bus_number=None, category=None, route_id=None):
        r =  {
            "status": "success",
            "fare": fare,
        }
        if bus_number:
            r["bus_number"] = bus_number
        if category:
            r["category"] = category
            if route_id:
                r["route_id"] = route_id
        return r
    

    @staticmethod
    def render_tickets(tickets):
        all_tickets = []
        for ticket_details in tickets:
            ticket_info = {
                'ticket_id': ticket_details['ticket_id'],
                'bus_number': ticket_details['bus_no'],
                'price': ticket_details['price'],
                'gender': ticket_details['gender'],
                'category': ticket_details['category'],
                'date_of_tickets': str(ticket_details['date_of_tickets']),
                'starting_stop_number': ticket_details['starting_stop_name'],
                'ending_stop_number': ticket_details['ending_stop_name'],
                'time_of_booking': str(ticket_details['time_of_booking'])
            }
            all_tickets.append(ticket_info)
        return all_tickets
         
    @staticmethod
    def render_error(message):
        return {
            "status": "error",
            "message": message
        }

    
    @staticmethod
    def render_links():
        links = {'create_user':'http://127.0.0.1:5002/users/create','login_user':'http://127.0.0.1:5002/users/login', 'create_employee':'http://127.0.0.1:5002/employee', 'login_employee':'http://127.0.0.1:5002/employee', 'bus route by bus number':'http://127.0.0.1:5001/buses/routes/<bus_number>', 'all bus route':'http://127.0.0.1:5001/buses', 'path between stops':'http://127.0.0.1:5001/buses/path/<int:stop1>/<int:stop2>'}
        return links
    







    

    