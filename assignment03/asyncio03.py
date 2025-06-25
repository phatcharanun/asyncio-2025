# example of creating an event loop
import asyncio
async def say_after(delay,msg):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    task1 =asyncio.create_task(say_after(1,"hello"))
    task2 =asyncio.create_task(say_after(2,"world"))
    
    await task1
    await task2

asyncio.run(main())