# check the type of a coroutine
import asyncio
#define a coroutine
async def custom_coro():
    #awit another coroutine
    await asyncio.sleep(1)

#create the coroutine
coro = custom_coro()
#chek the type of the coroutine
print(type(coro))