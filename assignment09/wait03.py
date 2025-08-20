#example of waiting for all tasks to complete
from random import random
import asyncio

#coroutine to execute in a new task
async def task_coro(arg):
    #generate a random value between 0 and 1
    value = random()
    #block for a moment
    await asyncio.sleep(value)
    #report the value
    print(f">task {arg} done with {value}")
    #conitionally fail
    if value < 0.5:
        raise Exception(f"Something bad happened in {arg}")
    
    #main coroutine 
async def main():
    #create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    #wait for the first thask to fail, or all tasks complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    #report results
    for task in done:
        if task.done():
            print(f"Done: {task.exception()}")

#start the asynio program
asyncio.run(main())