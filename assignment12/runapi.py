import asyncio
import httpx
import json

# รายการเครื่อง server
SERVERS = [
    "http://172.20.49.12",
    "http://172.20.49.56",
    "http://172.20.49.55",
    "http://172.20.50.40"
]

async def fetch_server(server_url: str):
    """ยิง request ไปที่ server แต่ละตัว"""
    async with httpx.AsyncClient() as client:
        try:
            r1 = await client.get(f"{server_url}:8000/Students")
            r2 = await client.get(f"{server_url}:8000/analytics/group")
            r3 = await client.get(f"{server_url}:8000/analytics/year")

            print(f"\n================ {server_url} ================")

            print("📌 Students")
            print(json.dumps(r1.json(), indent=2, ensure_ascii=False))

            print("\n📌 Analytics by Group")
            print(json.dumps(r2.json(), indent=2, ensure_ascii=False))

            print("\n📌 Analytics by Year")
            print(json.dumps(r3.json(), indent=2, ensure_ascii=False))

        except Exception as e:
            print(f"\n❌ Error fetching from {server_url}: {e}")

async def main():
    # ยิงพร้อมกันทุก server
    tasks = [fetch_server(s) for s in SERVERS]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
