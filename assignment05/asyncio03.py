# example of waiting for the first task to fail
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
    #conditionally fail
    if Value < 0.1:
        raise Exception(f'Something bad happened in {arg}')
    
#main coroutine
async def main():
    #create many tasks
    tasks = [asyncio.create_task(task_coro(i))for i in range(10)]
    #wait for all task to complete
    done,pening =await asyncio.wait(tasks , return_when=asyncio.FIRST_COMPLETED)
    #report result
    print ('Done')
    #get the first task to fail
    first = done.pop()
    print(first)

#start the asynio program
asyncio.run(main())