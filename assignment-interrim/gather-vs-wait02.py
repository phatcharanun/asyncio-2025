import asyncio

async def task_ok(n):
    await asyncio.sleep(n)
    return f"OK after {n} seconds"

async def task_error(n):
    await asyncio.sleep(n) 
    raise ValueError(f"Error after {n} seconds")

async def demon_wait():
    print("\n=== wait: check status ===")
    tasks = {asyncio.create_task(task_ok(1)), asyncio.create_task(task_ok(2))}
    done, pending = await asyncio.wait(tasks)
    print(f"Done tasks: {[t.result() for t in done]}")
    print(f"Pending tasks: {pending}")

    print("\n=== wait: handle errors manually ===")
    tasks = {asyncio.create_task(task_ok(1)), asyncio.create_task(task_error(2))}
    done, pending = await asyncio.wait(tasks)
    for t in done:
        exc = t.exception()
        if exc is None:
            print(f"Result: {t.result()}")
        else:
            print(f"Error: {exc}")


    print("\n=== wait: FIRST_COMPLETED ===")
    tasks = {asyncio.create_task(task_ok(1)), asyncio.create_task(task_ok(3))}
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(f"First done tasks: {[t.result() for t in done]}")
    print(f"Still pending tasks:", len(pending), "tasks(s)")

async def main():
    await demon_wait()
    
asyncio.run(main())