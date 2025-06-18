# Synchronous cooking
# 1 kitchen 1 chefs 1 dish
from time import sleep, ctime, time

# Cooking synchronous
def cooking(index):
    print(f'{index}: Kitchen-{index} : Begin cooking...')
    sleep(2)
    print(f'{index}: Kitchen-{index} : Cooking done!')

if __name__ == '__main__':
    # Begin of main thread
    print(f'{ctime} Main  : Start Cooking.')
    start_time = time()
    # Cooking
    cooking(0)
    
    duration = time() - start_time
    print(f'{ctime} Main  : Finished Cooking duration {duration:0.2f} seconds')