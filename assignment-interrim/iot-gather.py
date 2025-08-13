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
    tasks = [
        asyncio.create_task(get_temperature()),
        asyncio.create_task(get_humidity()),
        asyncio.create_task(get_weather())
    ]
    
    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks)
    
    for result in results:
        print(result)
    end = time.time()
    print(f"Took {end - start:.2f} seconds")
    
asyncio.run(main())