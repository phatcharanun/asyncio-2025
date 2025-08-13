import asyncio
import time
import random

async def save_to_db(sensor_id, value):
    await asyncio.sleep(1)  # Simulate a database save delay for 1 second
    if value > 80:
        raise ValueError(f"Sensor {sensor_id}: Value is too high!")
    print(f"[{time.ctime():} Saved0 {sensor_id} = {value}")

async def handle_sensor(sensor_id):
    value = random.randint(50, 100)  # Simulate sensor reading
    print(f"[{time.ctime():}] Sensor {sensor_id} got value: {value}")
    asyncio.create_task(save_to_db(sensor_id, value))  # Fire and forget / no await

async def main():
    for i in range(5):
        await handle_sensor(i)
    await asyncio.sleep(0.5)  # Simulate time between sensor readings

asyncio.run(main())