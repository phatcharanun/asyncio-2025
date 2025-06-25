# example of starting many tasks and getting access to all tasks
import time
import asyncio

#coroutine for a task
async def downlonad_image(name,delay):
    print(f"{time.ctime()} {name} กำลังโหลด...")
    await asyncio.sleep(delay)
    print(f"{time.ctime()} {name} โหลดเสร็จแล้ว!...")

#define a main coroutine
async def main():
    #report a message
    print(f'{time.ctime()}main coroutine started')
    #start many tasks
    started_tasks = [asyncio.create_task(downlonad_image(i,i))for i in range(3)]
    #allow some of the time to start
    await asyncio.sleep(0.1)
    for task in started_tasks:
        await task

#start the asycio program
asyncio.run(main())


