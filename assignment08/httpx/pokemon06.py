import asyncio
import httpx

ABILITYURL_list = "https://pokeapi.co/api/v2/ability/?limit=20"
def count_pokemon_in_ability(data):#นับจำนวน Pokémon ที่มี ability นั้น
    name = data["name"]
    pokemon_list = data["pokemon"]
    return name, len(pokemon_list)#

async def fetch_ability_detail(url, client):
    response = await client.get(url)
    return response.json()

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get(ABILITYURL_list)# ดึงรายการ abilities
        abilities = response.json()["results"][:10]  # ดึงแค่ 10 รายการแรก
        tasks = []
        for item in abilities:
            url = item["url"]# ดึง URL ของ ability
            # สร้าง task สำหรับดึงข้อมูล ability detail
            tasks.append(fetch_ability_detail(url, client))

        # ดึงข้อมูล
        ability_details = await asyncio.gather(*tasks)
        
        for detail in ability_details:
            name, count = count_pokemon_in_ability(detail)
            print(f"{name:<15} -> {count:<3} Pokemon")

    
if __name__ == "__main__":
    asyncio.run(main())
