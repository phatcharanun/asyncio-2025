import asyncio
import httpx

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://www.example.com')
        print(f"Status code: {response.status_code}")
        print(f"Response body: {response.text[:100]}...")

asyncio.run(main())