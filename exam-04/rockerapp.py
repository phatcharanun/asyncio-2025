# file: rocketapp.py

from fastapi import FastAPI, HTTPException
import asyncio
import random

app = FastAPI(title="Asynchronous Rocket Launcher")

# เก็บ task ของจรวด (optional)
rockets = []

async def launch_rocket(student_id: str):
    await asyncio.sleep(random.uniform(1, 2))
    print(f"Rocket launched for student {student_id}")
    print(f"Rocket for student {student_id} reached destination")
    return random.uniform(1, 2)

    """
    TODO:
    - จำลองเวลาจรวดด้วย random delay 1-2 วินาที
    - print log ว่า rocket launched และ reached destination
    """
    pass

@app.get("/fire/{student_id}")
async def fire_rocket(student_id: str):
    if len(student_id) != 10 or not student_id.isdigit():
        raise HTTPException(status_code=400, detail="student_id must be 10 digits")
    time_to_target = await launch_rocket(student_id)
    return {"message": f"Rocket launched for student {student_id}", "time_to_target": time_to_target}
    """
    TODO:
    - ตรวจสอบ student_id ต้องเป็น 10 หลัก
    - สร้าง background task ยิง rocket
    - รอ random delay 1-2 วินาที ก่อนส่ง response
    - return dict {"message": ..., "time_to_target": ...}
    """
    pass
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app, host=")
