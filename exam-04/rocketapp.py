from fastapi import FastAPI, HTTPException
import asyncio
import random

app = FastAPI(title="Asynchronous Rocket Launcher")

# เก็บ task ของจรวด (optional)
rockets = []


async def launch_rocket(student_id: str, time_to_target: float):
    """
    จำลองเวลาจรวดด้วย random delay 1-2 วินาที
    print log ว่า rocket launched และ reached destination
    """
    print(f"Rocket {student_id} launched! ETA: {time_to_target:.2f} seconds")
    await asyncio.sleep(time_to_target)
    print(f"Rocket {student_id} reached destination after {time_to_target:.2f} seconds")


@app.get("/fire/{student_id}")
async def fire_rocket(student_id: str):
    """
    - ตรวจสอบ student_id ต้องเป็น 10 หลัก
    - สร้าง background task ยิง rocket
    - random delay 1-2 วินาที
    - return dict {"message": ..., "time_to_target": ...}
    """
    # ตรวจสอบ student_id
    if not (student_id.isdigit() and len(student_id) == 10):
        raise HTTPException(status_code=400, detail="Invalid student_id. Must be 10 digits.")

    # สุ่มเวลาไปถึงเป้าหมาย
    time_to_target = round(random.uniform(1, 2), 2)

    # ยิง rocket เป็น background task
    task = asyncio.create_task(launch_rocket(student_id, time_to_target))
    rockets.append(task)

    # ส่ง response กลับทันที
    return {
        "message": f"Rocket {student_id} fired!",
        "time_to_target": time_to_target
    }
