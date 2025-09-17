# Hint:
# จุดผิด: t.result() ถูกเรียกก่อน task เสร็จ → เกิด InvalidStateError
# ให้แก้ไขโค้ดให้รอ task เสร็จก่อนแล้วจึงดึงผลลัพธ์
# Result:
# Worker 0 starting
# Worker 1 starting
# Worker 2 starting
# Worker 0 finished
# Worker 1 finished
# Worker 2 finished
# Result: [None, None, None]

import asyncio

async def worker(i):
    print(f"Worker {i} starting")
    await asyncio.sleep(i)
    print(f"Worker {i} finished")

async def main():
    tasks = [asyncio.create_task(worker(i)) for i in range(3)]
    for t in tasks:
        t.result()

asyncio.run(main())