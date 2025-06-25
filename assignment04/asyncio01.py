# example of getting the current task from the main coroutine
import asyncio

#define a main coroutine
async def main():
    #report a message
    print('main coroutine started')
    #get the curren task
    task = asyncio.current_task()
    #report its details
    print(task)

#star the asyncio program
asyncio.run(main())


    