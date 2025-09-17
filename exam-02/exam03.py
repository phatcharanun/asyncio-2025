# สร้างโปรแกรม อะซิงโครนัส ที่รัน countdown timers หลายตัวพร้อมกัน
# นักศึกษาต้องสร้างฟังก์ชัน countdown(name, seconds) ที่
#   1. พิมพ์ "Timer {name} starting for {seconds} seconds"
#   2. นับถอยหลังจาก seconds → 1
#   3. ทุกวินาที พิมพ์ "Timer {name}: {remaining} seconds left"
#   4. เมื่อครบเวลาพิมพ์ "Timer {name} finished"
# ใน main()
#   1. สร้าง countdown 3 ตัว เช่น ("A", 3), ("B", 5), ("C", 2)
#   2. รัน ทุก countdown พร้อมกัน โดยใช้ asyncio.create_task()
#   3. รอให้ทุก countdown เสร็จ
# นักศึกษาต้องเติม ส่วนการสร้าง task และ await

# Result:
# Timer A starting for 3 seconds
# Timer A: 3 seconds left
# Timer B starting for 5 seconds
# Timer B: 5 seconds left
# Timer C starting for 2 seconds
# Timer C: 2 seconds left
# Timer A: 2 seconds left
# Timer B: 4 seconds left
# Timer C: 1 seconds left
# Timer A: 1 seconds left
# Timer B: 3 seconds left
# Timer C finished
# Timer A finished
# Timer B: 2 seconds left
# Timer B: 1 seconds left
# Timer B finished


import asyncio

async def countdown(name: str, seconds: int):
    print(f"Timer {name} starting for {seconds} seconds")
    for i in range(seconds, 0, -1):
        print(f"Timer {name}: {i} seconds left")
        await asyncio.sleep(1)
    print(f"Timer {name} finished")

async def main():
    timers = [("A", 3), ("B", 5), ("C", 2)]
    
    tasks = []
    # TODO: สร้าง asyncio task สำหรับแต่ละ countdown
    # hint: ใช้ asyncio.create_task(countdown(name, sec))
    
    # TODO: รอให้ทุก task เสร็จ
    # hint: ใช้ await หรือ asyncio.gather(*tasks)
    pass

asyncio.run(main())