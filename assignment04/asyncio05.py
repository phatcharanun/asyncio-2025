# Check if a Task is Done
import asyncio

async def simple_task():
    await asyncio.sleep(1)
    return"เสร้จเเล้ว"

async def main():
    task = asyncio.create_task(simple_task())
    print("ก่อน await:",task.done()) #ยังไม่เสร้จ
    await task
    print ("หลัง await:",task.done())# เสร้จแล้ว

asyncio.run(main())

