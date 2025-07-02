# example of waiting for all tasks to complete
from random import random
import asyncio

#corotine to execte in a new task
async def task_coro(arg):
    #generate a random value beteen 0 and 1
    Value = random()
    #block for a momet
    await asyncio.sleep(Value)
    #report for value
    print(f'>task {arg} done with {Value}')

#main corotine
async def main():
    #create many tasks
    tasks = [asyncio.create_task(task_coro(i))for i in range(10)]
    #wait for all task to complete
    #done,pending = await asyncio.wait(tasks,return_whe=asynio.ALL_COMPLTED)
    done,pending = await asyncio.wait(tasks)
    #report results
    print ('ALL done')

#start the asynio program
asyncio.run(main())