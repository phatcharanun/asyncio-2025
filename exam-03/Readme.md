# Async Rocket Launcher – Single Student, 5 Rockets

## **โจทย์**

นักศึกษาจะต้องพัฒนา **โปรแกรม Python** เพื่อยิง **จรวด 3 ลูกพร้อมกัน** ไปยัง **rocketapp** ของอาจารย์ โดยใช้ **รหัสนักศึกษาเดียวกัน** (`student_id`) สำหรับทุกลูก

โปรแกรมต้องทำงานดังนี้:

1. แสดงข้อความตอนเริ่ม main:

   ```
   Rocket prepare to launch ...
   ```
2. ยิง **3 rockets พร้อมกัน** ด้วย `asyncio`
3. สำหรับแต่ละ rocket แสดง:

   * `start_time` (สัมพัทธ์จาก 0.0 sec)
   * `time_to_target` (จาก API response)
   * `end_time` (สัมพัทธ์จาก 0.0 sec)
4. เรียงลำดับ **rocket ตามเวลาที่ถึงจุดหมาย**
5. แสดง **เวลารวมทั้งหมด** ตั้งแต่ยิงลูกแรกจนลูกสุดท้ายถึงจุดหมาย

**Hint:**

* ใช้ `asyncio.create_task` เพื่อยิง rocket พร้อมกัน
* ใช้ `await asyncio.gather(*tasks)` เพื่อรอทุก rocket เสร็จ
* ใช้ `httpx.AsyncClient` หรือ `aiohttp` สำหรับ GET request แบบ async
* ใช้ `time.perf_counter()` สำหรับจับเวลา

---

# Result
```sh
Rocket prepare to launch ...
Rockets fired:
Rocket-1 | start_time: 0.00 sec | time_to_target: 1.73 sec | end_time: 1.73 sec
Rocket-2 | start_time: 0.01 sec | time_to_target: 1.85 sec | end_time: 1.86 sec
Rocket-3 | start_time: 0.01 sec | time_to_target: 1.66 sec | end_time: 1.67 sec

Total time for all rockets: 1.86 sec
```