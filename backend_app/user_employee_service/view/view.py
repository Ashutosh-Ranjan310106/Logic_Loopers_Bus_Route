from flask import render_template

class view:
    def render_error(msg, user_id = None):
        temp = {'error':msg}
        if user_id:
            temp['user_id'] = user_id
        return render_template('error.html', error_message=temp['error'])
    def render_successful(msg, user_id = None):
        temp = {'successful':msg}
        if user_id:
            temp['user_id'] = user_id
        return temp
    