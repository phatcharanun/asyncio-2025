# example of running a coroutine
import asyncio
#define a coroutine
async def custom_coro():
    #awit another coroutine
    await asyncio.sleep(1)

#main coroutine
async def main():
    #execue my custom corooutine
    await custom_coro

#STArt the coroutine program
asyncio.run(main())
