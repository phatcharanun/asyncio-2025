# example of waiting for all tasks to be completed with a timeout
from random import random
import asyncio

#corotine to execte in a new task
async def task_coro(arg):
    #generate a random value beteen 0 and 10
    Value = random()
    #block for a momet
    await asyncio.sleep(Value)
    #report for value
    print(f'>task {arg} done with {Value}')
    return f"task {arg} with {Value}"

#main coroutine
async def main():
    #create many tasks
    tasks = [asyncio.create_task(task_coro(i))for i in range(10)]
    #wait for all task to complete
    done,pneding = await asyncio.wait(tasks , timeout=0.5)
    #report results
    print (f'Done,{len(done)} tasks completed in time')
    

#start the asynio program
asyncio.run(main())