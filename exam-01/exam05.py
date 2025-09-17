# Hint:
# ให้แก้ไขให้โปรแกรมนับถอยหลังได้ถูกต้อง
# Result:
# T-minus 3
# T-minus 2
# T-minus 1

import asyncio

async def countdown(n):
    while n > 0:
        print("T-minus", n)
        #asyncio.sleep(1)
        await asyncio.sleep(1)
        n -= 1

async def main():
    await countdown(3)

asyncio.run(main())

