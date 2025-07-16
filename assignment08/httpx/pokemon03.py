# import requests
# import time

# start = time.time()

# url = f'https://pokeapi.co/api/v2/pokemon/pikachu'
# response = requests.get(url)
# data = response.json()
# print(f"{data['name'].title()} - ID: {data['id']},Height: {data["height"]},Weight: {data['weight']}, Types: {[t['type']['name'] for t in data['types']]}")

# end = time.time()
# print("total time:",round( end - start, 2), "seconds" )

import asyncio
import httpx
import time

async def fetch_pokemon( name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        print(f"{data['name'].title()} - ID: {data['id']}, Height: {data['height']}, Weight: {data['weight']}, Types: {[t['type']['name'] for t in data['types']]}")

async def main():
    start = time.time() 
    await fetch_pokemon("pikachu")
    end = time.time()
    print("total time:", round(end - start, 2), "seconds")

if __name__ == "__main__":
    asyncio.run(main())