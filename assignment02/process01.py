# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
import multiprocessing
import os
from time import sleep, ctine, time

def cooking(index):
    cooking_time = time()
    print(f'(ctime()) Kitchen-(index)   : Begin cooking...PID (os.getpid()))' )
    sleep(2)
    duration = time() - cooking_time
    print(f'(ctime()) Kitchen-(index) : Cooking done in <duration:0.2f) seconds!')

def kitchen(index):
    cooking(index)

if __name__=="__main__":
    #Begin of main thread
    print(f'(ctime()) Main : starting cook.')
    start_time = time()

    