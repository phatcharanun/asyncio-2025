# get result
import asyncio

async def simple_task():
    await asyncio.sleep(1)
    return"โหลด เสร็จ"

async def main():
    task = asyncio.create_task(simple_task())
    await task
    print("ผลลัพธ์ Task:",task.result())

asyncio.run(main())
    