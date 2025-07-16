import requests

url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
response = requests.get(url)

date = response.json()

print(f"Name: {date['name']}")
print(f"ID: {date['id']}")
print(f"Height: {date['height']}")
print(f"Weight: {date['weight']}")
print("Types", [t["type"]["name"] for t in date["types"]])