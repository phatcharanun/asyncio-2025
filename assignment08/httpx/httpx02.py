import asyncio
import httpx

async def fetch(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return url, response.status_code

async def main():
    urls = [
        'https://www.example.com',
        'https://www.python.org',
        'https://www.asyncio.org',
        'https://www.github.com'
    ]
    
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    
    for url, status in results:
        print(f"URL: {url}->{status}")
        
asyncio.run(main())  