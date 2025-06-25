# task name
import asyncio

async def simple_task():
    await asyncio.sleep(1)

async def main():
    task = asyncio.create_task(simple_task(),name=("โหลดช้อมูล"))
    print("ชื่อ Task:",task.get_name())
    await task

asyncio.run(main())