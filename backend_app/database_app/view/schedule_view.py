from flask import jsonify
class ScheduleView:
    @staticmethod
    def render_Schedule(schedules):
        # Convert schedules to a JSON-serializable format
        json_schedules = []
        for schedule in schedules:
            json_schedule = {
                'schedule_id': schedule['schedule_id'],
                'schedule_date': schedule['schedule_date'].isoformat(),  # Convert date to string
                'route': schedule['route'],
                'time': str(schedule['time']),  # Convert timedelta to string
                'route_id': schedule['route_id'],
                'start_node_number': schedule['start_node_number'],
                'stop_node_number': schedule['stop_node_number'],
                'bus_id': schedule['bus_id'],
                'conductor_id': schedule['conductor_id'],
                'driver_id': schedule['driver_id']
            }
            json_schedules.append(json_schedule)
        
        return jsonify(json_schedules)