# Race Conditions
import concurrent.futures
import logging
import time

class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)

    logging.info("Testing update. Ending value is %d.", database.value)

# Race conditions can occur when two or more threads access a shared piece of data or resource.
# Since each thread runs .update(), and .update() adds one to .value, you might expect database.value to be 2 when it’s printed out at the end.

