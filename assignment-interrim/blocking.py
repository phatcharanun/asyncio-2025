import asyncio, time;
async def say_after(delay, msg):
    if msg == "World":
        print(f"[{time.ctime():}] {msg} is blocking..... {delay} seconds")
        time.sleep(delay)  # Blocking call
    else:
        print(f"[{time.ctime():}] {msg} is non-blocking..... {delay} seconds")
        await asyncio.sleep(delay)

async def main():
    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(5, "World"))
    await task2
    await task1

asyncio.run(main())
print(f"[{time.ctime():}] All tasks completed.")