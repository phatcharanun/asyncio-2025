import asyncio
import time
import random
import aiohttp

urls = [
    "https://example.com",
    "https://httpbin.org/get",
    "https://python.org"
]

async def fetch (url):
    print(f"[{time.ctime():}] Fetching {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            print(f"[{time.ctime():}] Done {url} ({len(text)} bytes)")
            return url, len(text)

async def main():
    random_urls = random.sample(urls, len(urls))

    print("Random order:, random_urls")

    tasks = [asyncio.create_task(fetch(url)) for url in random_urls]
    results = await asyncio.gather(*tasks)
    print("Results:", results)

asyncio.run(main())