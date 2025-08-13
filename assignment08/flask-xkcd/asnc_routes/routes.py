import time
import random
import httpx  # ใช้แทน requests
from flask import Blueprint, render_template, current_app
import asyncio

# Create a Blueprint for async routes
async_bp = Blueprint("async", __name__)

# Async helper to fetch a single XKCD comic
async def get_xkcd(url, client):
    response = await client.get(url)
    print(f"{time.ctime()} - get {url}")    # Log
    return response.json()

# Async helper to fetch multiple XKCD comics concurrently
async def get_xkcds():
    NUMBER_OF_XKCD = current_app.config["NUMBER_OF_XKCD"]

    rand_list = [random.randint(0, 300) for _ in range(NUMBER_OF_XKCD)]

    
    async with httpx.AsyncClient() as client:
        tasks = []
        for number in rand_list:
            url = f'https://xkcd.com/{number}/info.0.json'
            tasks.append(get_xkcd(url, client))

        xkcd_data = await asyncio.gather(*tasks)
        return xkcd_data
    
# Route: GET /
@async_bp.route('/')
async def home():
    start_time = time.perf_counter()

    xkcds = await get_xkcds()  # ✅ await async fetch

    end_time = time.perf_counter()
    print(f"{time.ctime()} - Get {len(xkcds)} xkcd. Time taken: {end_time - start_time:.2f} seconds")

    return render_template('async.html',
                           title="XKCD Asynchronous Flask",
                           heading="XKCD Asynchronous Version",
                           xkcds=xkcds,
                           end_time=end_time,
                           start_time=start_time)
