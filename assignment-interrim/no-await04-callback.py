import asyncio
import time
import random

async def save_to_db(sensor_id, value):
    await asyncio.sleep( random.uniform(0.5,1.5))  # Simulate a database save delay for 1 second
    if value > 80:
        raise ValueError(f"Sensor {sensor_id}: Value is too high!")
    return f"[{sensor_id}] Saved value: {value}"

def task_done_callback(task):
    try:
        result = task.result()  # Get the result of the task / ดึงผลลัพธ์ถ้าม ี error จะ rasie ทันที
        print(f"Task completed successfully: {result}")
    except Exception as e:
        print(f"Task failed: {e}")

async def handle_sensor(sensor_id):
    value = random.randint(50, 100)  # Simulate sensor reading
    print(f"[{time.ctime():}] Sensor {sensor_id} got value: {value}")

    task = asyncio.create_task(save_to_db(sensor_id, value))  # Fire and forget / no awai
    task.add_done_callback(lambda t: print(t.result() if t.exception() is None else f"Error: {t.exception()}"))  # Handle result or error

async def main():
    for i in range(5):
        await handle_sensor(i)
    await asyncio.sleep(2)  # Simulate time between sensor readings

asyncio.run(main())