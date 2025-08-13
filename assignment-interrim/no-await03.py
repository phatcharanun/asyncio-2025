import asyncio ,time

async def worker_long():
    print(f"{time.ctime():} [Worker_Long ] Strt")
    try:
        await asyncio.sleep(5)  # speed long delay
        print(f"{time.ctime():} [Worker_Long ] Done")
    except asyncio.CancelledError:
        print(f"{time.ctime():} [Worker_Long ] cancelled!")

async def main():
    print(f"{time.ctime():} Start Main loop....")
    asyncio.create_task(worker_long()) 
    await asyncio.sleep(1)#main loop finished before worker_long()
    print(f"{time.ctime():} Main loop finished...!")

asyncio.run(main())