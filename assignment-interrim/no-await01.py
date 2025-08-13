import asyncio, time

async def worker_ok():
    print(f"[{time.ctime():}] [Worker_OK] started")
    await asyncio.sleep(1) 
    print(f"[{time.ctime():}] [Worker_OK] Done")

async def main():
    asyncio.create_task(worker_ok()) # fire-and-forget
    await asyncio.sleep(2) #wait for worker_ok completed job

asyncio.run(main())