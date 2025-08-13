import asyncio

async def task_ok(n):
    await asyncio.sleep(n)  # Simulate some work
    return f"OK after {n} seconds"

async def task_error(n):
    await asyncio.sleep(n)  # Simulate some work
    raise ValueError(f"Error after {n} seconds")

async def demon_gather():
    print("\n=== gather: returns values ===")
    results = await asyncio.gather(task_ok(1),task_ok(2))
    print (f"Gather results: {results}")

    print("\n=== gather: error stops all ===")
    try:
        await asyncio.gather(task_ok(1), task_error(2))
    except Exception as e:
        print(f"Caught:", repr(e))

    print("\n=== gather: return_exceptions=True ===")
    results = await asyncio.gather(task_ok(1), task_error(2), 
    return_exceptions=True)
    print(f"Gather results : {results}")

async def main():
    await demon_gather()
    
asyncio.run(main())