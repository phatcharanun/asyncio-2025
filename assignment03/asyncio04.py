# Starting task Even loop
import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(greet())# สร้างและรัน event loop

#
#loop = asynic.new_eveny_loop
#asyncio.set_event_loop(loop)
# loop.run_until_complete(greet())
# loop.close()