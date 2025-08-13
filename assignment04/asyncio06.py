# check_cancelled.py
import asyncio

async def slow_task():
    await asyncio.sleep(5)

async def main():
    task =asyncio.create_task(slow_task())
    await asyncio.sleep(1)
    task.cancel()
    try :
        await task
    except asyncio.CancelledError:
        print("Task ยกเลิก:" ,task.cancelled()) #true

asyncio.run(main())

        