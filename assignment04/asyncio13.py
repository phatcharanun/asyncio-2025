# all tasks
import asyncio

async def dummy():
    await asyncio.sleep(2)

async def main():
    t1= asyncio.create_task(dummy(),name="Task A")
    t2 = asyncio.create_task(dummy(), name="Task B")
    await asyncio.sleep(0.1)

    all_tasks = asyncio.all_tasks()
    print("Task ทั้งหมด loop:")
    for t in all_tasks:
        print(" -",t.get_name())

asyncio.run(main())