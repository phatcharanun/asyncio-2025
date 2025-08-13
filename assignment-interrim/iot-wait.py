import asyncio, time, random

async def get_temperature():
    await asyncio.sleep(random.uniform(0.5, 2))  # Simulate sensor reading delay
    return f"{time.ctime()}: Temperature: 30°C"

async def get_humidity():
    await asyncio.sleep(random.uniform(0.5, 2))  # Simulate sensor reading delay
    return f"{time.ctime()}: Humidity: 60%"

async def get_weather():
    await asyncio.sleep(random.uniform(0.5, 2))  # Simulate sensor reading delay
    return f"{time.ctime()}: Weather: Sunny"

async def main():
    start = time.time()
    # Create tasks for each sensor reading
    tasks = {
        asyncio.create_task(get_temperature(), name="temp"),
        asyncio.create_task(get_humidity(),    name="humid"),
        asyncio.create_task(get_weather(),     name="weather"),
    }

    pending = set(tasks)
    while pending:
        done, pending = await asyncio.wait(
            pending, return_when=asyncio.FIRST_COMPLETED
        )
        for t in done:
            try:
                print(t.result())            # แสดงทันทีที่เสร็จ
            except Exception as e:
                print(f"[{t.get_name()}] error: {e}")

    end = time.time()
    print(f"Took {end - start:.2f} seconds")

asyncio.run(main())