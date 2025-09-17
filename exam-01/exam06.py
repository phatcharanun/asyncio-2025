# Hint:
# ปัญหา: asyncio.gather() จะ throw ข้อผิดพลาดทั้งหมด ไม่ใช่แค่ตัวแรก
# ให้แก้ไขโค้ดเพื่อให้สามารถ จัดการข้อผิดพลาดแยกแต่ละ task ได้
# Result:
# [ValueError('Something went wrong!'), ValueError('Something went wrong!')]

#ยังไม่
import asyncio

async def risky_task():
    raise ValueError("Something went wrong!")


async def main():

    try:
        await asyncio.gather(risky_task(), risky_task())

        
    except Exception as e:

        print("Caught:", e)
        
asyncio.run(main())


# async def risky_task():ต้นฉบับ
#     raise ValueError("Something went wrong!")

# async def main():
#     try:
#         await asyncio.gather(risky_task(), risky_task())
        
#     except Exception as e:
#         print("Caught:", e)
# asyncio.run(main())


# async def risky_task():
#     #raise ValueError("Something went wrong!")
#     try:
#        # await asyncio.gather(risky_task(), risky_task())
#         print("Caught:", e)
#     except Exception as e:
#         await asyncio.gather(risky_task(), risky_task())
#         return e
#         #print("Caught:", e)

# async def main():
#     re = await asyncio.gather(
#         risky_task(),
#         risky_task())
#     print("Results:", re)

#     #try:
#        # await asyncio.gather(risky_task(), risky_task())
#        # print("Caught:", e)
#     #except Exception as e:
#        # await asyncio.gather(risky_task(), risky_task())
#         #print("Caught:", e)
# asyncio.run(main())