import time
import random
import requests as requests
from flask import Blueprint, render_template, current_app

# Create a Blueprint for sync routes
sync_bp = Blueprint("sync", __name__)

# Helper function to fetch a single XKCD JSON by URL
def get_xkcd(url):
    response = requests.get(url)
    print(f"{time.ctime()} - get {url}")    # Log the request time and URL
    return response.json()

# Helper function to fetch multiple XKCD comics
def get_xkcds():
    # Get the number of comics to fetch from app config
    NUMBER_OF_XKCD = current_app.config["NUMBER_OF_XKCD"]

    # Generate a list of random comic numbers (0–300)
    rand_list=[]
    for i in range(NUMBER_OF_XKCD):
        rand_list.append(random.randint(0,300))

    xkcd_data = []
    for number in rand_list:
        url = f'https://xkcd.com/{number}/info.0.json'
        xkcd_json = get_xkcd(url)   # Fetch comic JSON
        xkcd_data.append(xkcd_json)
    return xkcd_data

# Route: GET /sync/
@sync_bp.route('/')
def home():
    start_time = time.perf_counter()  # Start performance timer
    xkcds = get_xkcds()               # Fetch random XKCD comics
    end_time = time.perf_counter()    # End performance timer

    # Log time and count
    print(f"{time.ctime()} - Get {len(xkcds)} xkcd. Time taken: {end_time-start_time} seconds")

    # Render result using Jinja2 template
    return render_template('sync.html'
                           , title="XKCD Synchronous Flask"
                           , heading="XKCD Synchronous Version"
                           , xkcds=xkcds
                           , end_time=end_time
                           , start_time=start_time)
