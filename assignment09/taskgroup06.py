import asyncio

async def safe_task(name, sec, fail=False):
    try:
        await asyncio.sleep(sec)
        if fail:
            raise ValueError(f"{name} failed")
        return f"{name} OK"
    except Exception as e:
        return f"{name} error: {e}"

async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(safe_task("A", 1, fail=True))
        t2 = tg.create_task(safe_task("B", 2))
        t3 = tg.create_task(safe_task("C", 3))

    print(t1.result())
    print(t2.result())
    print(t3.result())

asyncio.run(main())