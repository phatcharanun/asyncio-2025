import asyncio
import time
import random
import aiohttp

urls = [
    "https://example.com/",
    "https://httpbin.org/get",
    "https://python.org/",
]

async def fetch(url):
    print(f"[{time.ctime()}] Fetching {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            text = await resp.text()
            print(f"[{time.ctime()}] Done {url} ({len(text)} bytes)")
            return url, len(text)

async def main():
    random_urls = random.sample(urls, len(urls))  # Shuffle URLs
    print("Random order:", random_urls)

    coros = [fetch(url) for url in random_urls]

    results = await asyncio.gather(*coros)
    print("Results:", results)

asyncio.run(main())