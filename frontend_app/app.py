from flask import Flask, render_template, request

app = Flask(__name__)
appstate = 'himachi'
if appstate == 'production':
    host = '192.168.163.145'
elif appstate == 'himachi':
    host = '25.24.45.37'
else:
    host='127.0.0.1'
# User and Employee Management Module
@app.route('/user', methods=['GET'])
def user_index():
    return render_template('user/index.html')
@app.route('/user/create', methods=['GET'])
def user_create():
    return render_template('user/create.html')

@app.route('/user/login', methods=['GET'])
def user_login():
    return render_template('user/login.html')

@app.route('/user/ticket', methods=['GET'])
def user_ticket():
    return render_template('user/ticket.html')

@app.route('/user/fare', methods=['GET'])
def user_fare():
    return render_template('user/fare.html')



@app.route('/employee', methods=['GET'])
def employee_index():
    return render_template('employee/index.html')
@app.route('/employee/create', methods=['GET'])
def employee_create():
    return render_template('employee/create.html')

@app.route('/employee/login', methods=['GET'])
def employee_login():
    return render_template('employee/login.html')

@app.route('/employee/logout', methods=['GET'])
def employee_logout():
    return render_template('employee/logout.html')


# Buses Module
@app.route('/buses', methods=['GET'])
def buses():
    return render_template('buses/index.html')

@app.route('/buses/routes', methods=['GET'])
def bus_routes():
    return render_template('buses/routes.html')

@app.route('/buses/path', methods=['GET'])
def bus_path():
    return render_template('buses/path.html')

@app.route('/buses/schedule', methods=['GET'])
def bus_schedule():
    return render_template('buses/schedule.html')


# Database Management Module
@app.route('/database', methods=['GET'])
def database_index():
    return render_template('database/index.html')
@app.route('/database/stop', methods=['GET'])
def database_stop():
    return render_template('database/stop.html')

@app.route('/database/route', methods=['GET'])
def database_route():
    return render_template('database/route.html')

@app.route('/database/schedule', methods=['GET'])
def database_schedule():
    return render_template('database/schedule.html')

@app.route('/database/ticket', methods=['GET'])
def database_ticket():
    return render_template('database/ticket.html')

@app.route('/database/bus', methods=['GET'])
def database_bus():
    return render_template('database/bus.html')

@app.route('/database/staff', methods=['GET'])
def database_staff():
    return render_template('database/staff.html')

@app.route('/database/reachtime', methods=['GET'])
def database_reach_time():
    return render_template('database/reachtime.html')

@app.route('/render/tickets', methods=['GET'])
def render_tickets():
    ticket_data = eval(request.args.get('ticket_data'))
    return render_template('render/tickets.html', ticket_data=ticket_data)
@app.route('/render/schedule', methods=['GET'])
def render_schedule():
    schedules = eval(request.args.get('schedule_data'))
    return render_template('render/schedule.html', schedules=schedules)

@app.route('/render/routes', methods=['GET'])
def render_route():
    route = eval(request.args.get('route_data'))
    return render_template('render/route.html', route=route)

@app.route('/render/path', methods=['GET'])
def render_path():
    paths = eval(request.args.get('path_data'))
    return render_template('render/path.html', paths=paths)




if __name__ == '__main__':
    app.run(host=host, debug=True, port = 5004)
