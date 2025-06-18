# Working With Many Threads
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for index in range(3):
        logging.info("Main     : creata and start thread %d.",index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index,thread in enumerate(threads):
        logging.info("Main   : before joining thred %d.",index)
        thread.join()
        logging.info("Main     : thread %d Done",index)

# If you walk through the output carefully, you'll see all three threads getting 
# started in the order you might expect, but in this case they finish in the opposite
#order! Multiple runs will produce different orderings. Look for the Thread x:
#finishing message to tell you when each thread is done.   
# 
## The order in which threads are run is determined by the operating systen and can
#be quite hard to predict. It may (and likely will) vary from run to run, so you need
#to be aware of that when you design algorithms that use threading    