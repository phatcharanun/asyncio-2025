import time
import random
import httpx  # ใช้แทน requests ใน sync
from flask import Blueprint, render_template, current_app
import asyncio

# Create a Blueprint for async routes
async_bp = Blueprint("async", __name__)

# Async helper to fetch a single pokemon comic
async def get_pokemon(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print(f"{time.ctime()} - get {url}")    # Log
    return response.json()

# Async helper to fetch multiple pokemon comics concurrently
async def get_pokemons():
    NUMBER_OF_POKEMON = current_app.config["NUMBER_OF_POKEMON"]

    rand_list = [random.randint(0, 300) for _ in range(NUMBER_OF_POKEMON)]

    
    
    tasks = []
    for number in rand_list:
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        tasks.append(get_pokemon(url))
    xkcd_data = await asyncio.gather(*tasks)
    return xkcd_data
    
# Route: GET /
@async_bp.route('/')
def home():
    start_time = time.perf_counter()

    pokemons = asyncio.run(get_pokemons())  # ✅ await async fetch

    end_time = time.perf_counter()
    print(f"{time.ctime()} - Get {len(pokemons)} pokemon. Time taken: {end_time - start_time:.2f} seconds")

    return render_template('sync.html',
                           title="pokemon Asynchronous Flask",
                           heading="pokemon Asynchronous Version",
                           pokemons=pokemons,
                           end_time=end_time,
                           start_time=start_time)
