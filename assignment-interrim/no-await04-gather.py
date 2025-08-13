import asyncio
import time
import random

async def save_to_db(sensor_id, value):
    await asyncio.sleep(1)  # Simulate a database save delay for 1 second
    print (f"[{time.ctime():} Saved0 {sensor_id} = {value}")

async def main():
    tasks = [] # List to hold tasks (เก็บ task ไว้)
    for sensor_id in range(5):
        value = random.randint(50, 100)  # Simulate sensor reading
        print(f"[{time.ctime():}] Sensor {sensor_id} got value: {value}")
        task = asyncio.create_task(save_to_db(sensor_id, value)) # Fire and forget / no await
        tasks.append(task)  # Add task to the list
    
    # Wait for all tasks to complete / รอให้ task ทั้งหมดทำงานเสร็จ
    await asyncio.gather(*tasks)  # Wait for all tasks to complete

asyncio.run(main())