from flask import jsonify
class ScheduleView:
    @staticmethod
    def render_Schedule(schedules):
        json_schedules = []
        for schedule in schedules:
            json_schedule = {
                'schedule_id': schedule['schedule_id'],
                'schedule_day': schedule['schedule_day'],
                'route': schedule['route'],
                'time': str(schedule['time']),
                'route_id': schedule['route_id'],
                'start_stop_number': schedule['start_stop_number'],
                'stop_stop_number': schedule['stop_stop_number'],
                'bus_id': schedule['bus_id'],
                'conductor_id': schedule['conductor_id'],
                'driver_id': schedule['driver_id']
            }
            json_schedules.append(json_schedule)
        return json_schedules