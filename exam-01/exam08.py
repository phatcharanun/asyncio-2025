# Hint:
# โค้ดนี้จะทำงานได้ แต่เกิด ResourceWarning: Unclosed client session
# ให้นักศึกษาแก้ไขโดยใช้ async with aiohttp.ClientSession()
# Result:
# 1256

import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:  # ใช้ async with เพื่อให้ปิดอัตโนมัติ
        async with session.get(url) as resp:
            return await resp.text()

async def main():
    html = await fetch("https://example.com")
    print(len(html))

asyncio.run(main())
