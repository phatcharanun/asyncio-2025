# Create 2 Tasks with High-Level API
import asyncio

async def downlonad_image(name,delay):
    print(f"{name} กำลังโหลด")
    await asyncio.sleep(delay)
    print(f"{name} โหลดเสร็จแล้ว!")

async def main():
    #สร้าง task พร้อมกัน
    task1 = asyncio.create_task(downlonad_image("ภาพที่1",2))
    task2 = asyncio.create_task(downlonad_image("ภาพที่2",3))

    #รอให้ทั้งสอง task เสร้จ
    await task1
    await task2

asyncio.run(main())
