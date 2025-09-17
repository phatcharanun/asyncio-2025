
# โจทย์นักศึกษา: พัฒนา RocketApp ด้วย FastAPI

## **โจทย์**

นักศึกษาจะต้องพัฒนา **FastAPI server** (`rocketapp.py`) ให้ทำงานดังนี้:

1. เปิด server ด้วย **FastAPI**
2. สร้าง **endpoint**:

```
GET /fire/{student_id}
```

* ตรวจสอบว่า `student_id` ต้องเป็น **10 หลัก**
* ถ้าไม่ถูกต้อง → ส่ง HTTP 400

3. เมื่อยิง rocket:

* สร้าง **background async task** จำลอง rocket flight (`launch_rocket`)
* ใช้ **random delay 1–2 วินาที** เพื่อจำลองเวลาจรวดไปถึงเป้าหมาย
* พิมพ์ log:

```
Rocket {student_id} launched! ETA: X.XX seconds
Rocket {student_id} reached destination after X.XX seconds
```

4. **Response** ของ API `/fire/{student_id}` ต้องเป็น JSON เช่น:

```json
{
  "message": "Rocket 6410301001 fired!",
  "time_to_target": 1.53
}
```

* `time_to_target` → random 1–2 วินาที

5. รองรับ **หลาย request พร้อมกัน** แบบ async

---

## **Hints**

* ใช้ `asyncio.create_task()` เพื่อรัน rocket flight แบบ background
* ใช้ `asyncio.sleep()` สำหรับ delay
* ตรวจสอบ `student_id` ด้วย `len(student_id)` และ `isdigit()`
* FastAPI จะส่ง response JSON อัตโนมัติจาก dict

---

### FastAPI helper
```bash
pip install fastapi uvicorn
uvicorn rocketapp:app --reload --host 127.0.0.1 --port 8088
```