# Create 1 Task with High-Level API
import asyncio

async def do_something():
    print("เริ่มทำงาน..")
    await asyncio.sleep(2)
    print("ทำงานเสร้จแล้ว!")

async def main():
    task = asyncio.create_task(do_something())
    await task#รอให้trsk เสร้จ

asyncio.run(main())