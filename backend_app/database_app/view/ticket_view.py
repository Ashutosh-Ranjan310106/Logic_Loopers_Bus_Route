from flask import render_template
class TicketView:
    @staticmethod
    def render_ticket(ticket):
        ticket_data = {
            "ticket_id": ticket["ticket_id"],
            "route_id": ticket["route_id"],
            "price": ticket["price"],
            "gender": ticket["gender"],
            "category": ticket["category"],
            "date_of_tickets": ticket["date_of_tickets"].strftime("%Y-%m-%d"),
            "ticket_type": "offline",
            "direction": ticket["direction"],
            "status": "success"
        }

        return {"status": "success", "ticket": ticket_data}, 200
    @staticmethod
    def render_ticket_verification(tickets):
        ticket_data = {"message":[], "status":"success"}

        for ticket in tickets:
            ticket_data["message"].append({
                "ticket_id": ticket["ticket_id"],
                "route_id": ticket["route_id"],
                "price": ticket["price"],
                "gender": ticket["gender"],
                "category": ticket["category"],
                "ticket_type": ticket["ticket_type"],
                "date_of_tickets": str(ticket["date_of_tickets"])
            })

        return ticket_data
