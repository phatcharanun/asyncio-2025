import time
import requests as requests
from flask import Flask, render_template


from async_routes.routes import async_bp
from sync_routes.routes import sync_bp


# Initialize the Flask application
app = Flask(__name__)

app.register_blueprint(async_bp, url_prefix="/async")#------------------เพิ่มเติม-----------------
app.register_blueprint(sync_bp, url_prefix="/sync")
# Define constant using Flask's config dictionary
app.config["NUMBER_OF_POKEMON"] = 20  # Used to control how many pokemon to fetch

# Define root route
@app.route('/')
def index():
    start_time = time.perf_counter()  # Start timer
    end_time = time.perf_counter()    # End timer (immediate since no logic)

    # Render base template with performance timing and empty list
    return render_template('base.html'
                           , title="Flask pokemon"
                           , heading="Pokemon Flask"
                           , pokemon=[]   # Placeholder for pokemon or other items
                           , end_time=end_time, start_time=start_time)

# Run the application
if __name__ == '__main__':
    app.run(debug=True, port=50000)