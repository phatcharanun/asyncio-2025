# Hint:
# แก้โค้ดให้สามารถรัน หลาย task พร้อมกัน ได้ถูกต้อง
# Result:
# Processing data
# Processing data
# Processing data
# Processing data
# Processing data

import asyncio

# async def fetch_data():
#     textData = "Data" 
#     await asyncio.sleep(2)
#     #return "data"

async def process():
    # data = await fetch_data()
    print(f'Processing data')
async def main():
    tasks = asyncio.gather(*[process() for _ in range(5)])
    await asyncio.sleep(1)
   # tasks = [process() for _ in range(5)]
asyncio.run(main())

