# get Exception
import asyncio

async def error_task():
    await asyncio.sleep(1)
    raise ValueError("เกิดข้อผืดพลาด")

async def main():
    task = asyncio.create_task(error_task())
    try:
        await task
    except Exception:
        print("Exception ที่เกิด", task.exception())

asyncio.run(main())