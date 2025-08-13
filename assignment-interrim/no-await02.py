import asyncio, time

async def worker_ok():
    print(f"[{time.ctime():}] Worker OK is Starting")
    await asyncio.sleep(1)  
    raise ValueError("Boom!!!")  # raisr error

async def main():
    asyncio.create_task(worker_ok())
    await asyncio.sleep(2)  

asyncio.run(main())