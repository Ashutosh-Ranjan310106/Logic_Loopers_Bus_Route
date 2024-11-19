from flask import render_template, jsonify

class StopView:
    @staticmethod
    def render_stops(stops):
        return jsonify(stops)
        return render_template('stop_view.html', stops=stops)
