# cancel task
import asyncio

async def slow_task():
    await asyncio.sleep(3)

async def main():
    task =asyncio.create_task(slow_task())
    print("ยกเลิก task ใน 1 วิ")
    await asyncio.sleep(1)
    task.cancel()
    try :
        await task
    except asyncio.CancelledError:
        print("Task ถูก cancel แล้ว")

asyncio.run(main())