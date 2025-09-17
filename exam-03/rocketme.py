import time
import asyncio
import aiohttp

student_id = "6610301001"   # เปลี่ยนเป็น student_id ของนักศึกษา

async def fire_rocket(name: str, t0: float):
    url = f"http://172.16.2.117:8088/fire/{student_id}"
    start_time = time.perf_counter() - t0  # เวลาเริ่มสัมพัทธ์

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            time_to_target = data["time_to_target"]
            await asyncio.sleep(time_to_target)   # จำลองเวลาที่ใช้บิน
            end_time = time.perf_counter() - t0   # เวลาเสร็จสัมพัทธ์

    return {
        "name": name,
        "start_time": start_time,
        "time_to_target": time_to_target,
        "end_time": end_time
    }

async def main():
    t0 = time.perf_counter()  # เวลาเริ่มของชุด rockets

    print("Rocket prepare to launch ...")
    await asyncio.sleep(1)  # จำลองการเตรียมตัวก่อนยิง

    # ยิง rocket 3 ลูกพร้อมกัน
    rocket_names = ["Rocket1", "Rocket2", "Rocket3"]
    tasks = [asyncio.create_task(fire_rocket(name, t0)) for name in rocket_names]

    results = await asyncio.gather(*tasks)

    # เรียงลำดับตามเวลาที่ถึงเป้าหมาย (end_time)
    results_sorted = sorted(results, key=lambda r: r["end_time"])

    print("Rockets fired:")
    for r in results_sorted:
        print(f"{r['name']} | start_time: {r['start_time']:.2f} sec | "
              f"time_to_target: {r['time_to_target']:.2f} sec | "
              f"end_time: {r['end_time']:.2f} sec")

    # เวลารวมทั้งหมด (max end_time)
    t_total = max(r["end_time"] for r in results_sorted)
    print(f"\nTotal time for all rockets: {t_total:.2f} sec")

if __name__ == "__main__":
    asyncio.run(main())
