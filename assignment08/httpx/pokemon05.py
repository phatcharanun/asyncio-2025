import asyncio
import httpx
import time

# ดึงข้อมูล Pokemon แล้ว return dict
async def fetch_pokemon(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return {
            "name": data["name"].title(),
            "id": data["id"],
            "base_experience": data["base_experience"]
        }

# ฟังก์ชันสำหรับ sort ตาม base_experience
def get_base_xp(pokemon):
    return pokemon["base_experience"]

# main
async def main():
    pokemon_names = [
        "pikachu", "bulbasaur", "charmander", "squirtle",
        "eevee", "snorlax", "gengar", "mewtwo", "jigglypuff"
    ]
    
    start = time.time()

    tasks = [fetch_pokemon(name) for name in pokemon_names]
    results = await asyncio.gather(*tasks)

    # เรียงลำดับจากมากไปน้อยตาม base_experience
    sorted_pokemon = sorted(results, key=get_base_xp, reverse=True)

    for p in sorted_pokemon:
        print(f"{p['name']:<12} - ID: {p['id']:<5}, base_exp: {p['base_experience']:<5}")

    end = time.time()
    print("\nTotal time:", round(end - start, 2), "seconds")

if __name__ == "__main__":
    asyncio.run(main())



#ซิงโครนัส
# pokemon_names = ["pikachu",  "bulbasaur","charmander", "squirtle","eevee","snorlax"
#                  ,"gengar", "mewtwo", "jigglypuff"]

# start = time.time()

# for name in pokemon_names:
#     url = f'https://pokeapi.co/api/v2/pokemon/{name}'
#     response = requests.get(url)
#     data = response.json()
#     print(f"{data['name'].title()} - ID: {data['id']}, Types: {[t['type']['name'] for t in data['types']]}")

# end = time.time()
# print("total time:",round( end - start, 2), "seconds" )