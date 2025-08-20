import asyncio
import random

async def read_temperature():
    await asyncio.sleep(1)
    return f"Temperature: {random.randint(20, 35)} °C"

async def read_humidity():
    await asyncio.sleep(2)
    return f"Humidity: {random.randint(40, 70)} %"

async def read_pressure():
    await asyncio.sleep(3)
    return f"Pressure: {random.randint(900, 1100)} hPa"

async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(read_temperature())
        t2 = tg.create_task(read_humidity())
        t3 = tg.create_task(read_pressure())

    # มั่นใจว่าเสร็จทุก task
    print(t1.result())
    print(t2.result())
    print(t3.result())

asyncio.run(main())