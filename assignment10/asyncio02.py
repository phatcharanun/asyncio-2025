# example of using an asyncio queue without blocking
from random import random
import asyncio

#coroutine to generate work
async def producer(queue):
    print("Producer: Running")
    #generate work
    for i in range(10):
        #generate a value
        value = i
        #block to simulate work
        sleeptime = random()
        print(f'>producer {value} sleep {sleeptime} ')
        await asyncio.sleep(sleeptime)
        #add to the queue
        print(f'>Producer put {value}')
        await queue.put(value)
    #send an all done signal
    await queue.put(None)
    print("Producer: Done")

    #corotine to consume work
async def consumer(queue):
    print('Consumer: Running')
    #consume work
    while True:
        #get a unit of work withuot blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumwer:got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        #check for stop
        if item is None:
            break
        #report
        print(f'\t> Consumer got  {item}')
    #all done
    print("Consumer: Done")

#entry point coroutine
async def main():
    #create the shared queue
    queue = asyncio.Queue()
    #run the producer and consumer
    await asyncio.gather(producer(queue), consumer(queue))

#start the asncio program
asyncio.run(main())