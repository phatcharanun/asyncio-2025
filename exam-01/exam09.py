# Hint:
# การเรียก asyncio.run(main()) ซ้ำหลายครั้งในไฟล์เดียวกัน จะทำงานได้ในการรันครั้งแรก
# แต่ครั้งที่สองอาจเกิด RuntimeError หรือ loop ปิดแล้ว (ขึ้นกับเวอร์ชัน Python/สภาพแวดล้อม)
# สาเหตุคือ asyncio.run() จะ สร้าง event loop ใหม่ → รัน coroutine → ปิด loop
# ไม่ควรเรียกซ้ำหลายครั้ง แต่ควรรวมงานทั้งหมดไว้ใน main() แทน
# Result:
#   Start 0
#   Start 1
#   Start 2
#   Done 0
#   Done 1
#   Done 2
#   Results1: [0, 1, 2]
#   Start 3
#   Start 4
#   Start 5
#   Done 3
#   Done 4
#   Done 5
#   Results2: [3, 4, 5]

import asyncio

async def work(n):
    print(f"Start {n}")
    await asyncio.sleep(1)
    print(f"Done {n}")
    return n

async def main():
    results = []
    for i in range(3):
        results.append(asyncio.create_task(work(i)))
    for r in results:
        print("Result:", await r)

asyncio.run(main())
asyncio.run(main())