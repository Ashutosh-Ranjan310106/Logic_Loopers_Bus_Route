
from flask import render_template
from bus_app.service.service import BusService
class PathView:
    def render_path(paths):
        
        
        return paths
        return render_template('bus_paths.html', paths=paths)
