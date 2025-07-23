import time
import requests as requests
from flask import Flask, render_template

# Import blueprints from sync and async route folders
from sync_routes.routes import sync_bp

# Initialize the Flask application
app = Flask(__name__)

# Register sync and async blueprints under different URL prefixes
app.register_blueprint(sync_bp, url_prefix="/sync")

# Define constant using Flask's config dictionary
app.config["NUMBER_OF_XKCD"] = 7  # Used to control how many XKCD to fetch

# Define root route
@app.route('/')
def index():
    start_time = time.perf_counter()  # Start timer
    end_time = time.perf_counter()    # End timer (immediate since no logic)

    # Render base template with performance timing and empty list
    return render_template('base.html'
                           , title="Flask XKCD"
                           , heading="Pokemon Flask"
                           , xkcds=[]   # Placeholder for XKCD or other items
                           , end_time=end_time, start_time=start_time)

# Run the application
if __name__ == '__main__':
    app.run(debug=True, port=50000)