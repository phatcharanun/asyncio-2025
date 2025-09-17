import time
import asyncio
import aiohttp

student_id = "6610301001"   # เปลี่ยนเป็น student_id ของนักศึกษา

async def fire_rocket(name: str, t0: float):
    url = f"http://172.16.2.117:8088/fire/{student_id}"
    start_time = time.perf_counter() - t0  # เวลาเริ่มสัมพัทธ์
    end_time = None#เพิ่ม
    time_to_target = None


    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            time_to_target = data["time_to_target"]
            await asyncio.sleep(time_to_target)
            end_time = time.perf_counter() - t0  # เวลาเสร็จสัมพัทธ์
    return  {
            "name": name,
            "start_time": start_time,
            "time_to_target": time_to_target,
            "end_time": end_time
        }
    """
    TODO:
    - ส่ง GET request ไปยัง rocketapp ที่ path /fire/{student_id}
    - อ่านค่า time_to_target จาก response
    - return dict ที่มี:
        {
            "name": name,
            "start_time": start_time,
            "time_to_target": time_to_target,
            "end_time": end_time
        }
    """
    pass

async def main():
    t0 = time.perf_counter()  # เวลาเริ่มของชุด rockets

    print("Rocket prepare to launch ...")  # แสดงตอนเริ่ม main
    await asyncio.sleep(1)  # จำลองการเตรียม launchๆ
    

    # TODO: สร้าง task ยิง rocket 3 ลูกพร้อมกัน
    tasks = []
    rocket_names = ["Apollo", "Gemini", "Mercury"]#เพิ่ม
    for name in rocket_names:
        tasks.append(asyncio.create_task(fire_rocket(name, t0)))

    # TODO: รอให้ทุก task เสร็จและเก็บผลลัพธ์ตามลำดับ task
    results = []
    results = await asyncio.gather(*tasks)


    # TODO: แสดงผล start_time, time_to_target, end_time ของแต่ละ rocket ตามลำดับ task
    for r in results:
        print(f"Rocket {r['name']}: start at {r['start_time']:.2f} sec, "
              f"time to target {r['time_to_target']:.2f} sec, "
              f"end at {r['end_time']:.2f} sec")
        
        pass  # แสดงผล rocket
    print("All rockets have been launched.")


    # TODO: แสดงเวลารวมทั้งหมดตั้งแต่ยิงลูกแรกจนลูกสุดท้ายถึงจุดหมาย

    t_total = 0  # คำนวณ max end_time
    print(f"\nTotal time for all rockets: {t_total:.2f} sec")

