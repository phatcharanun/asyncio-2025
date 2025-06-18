import concurrent.futures
import logging
import threading
import time

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.info("Thread %s about to lock", name)
        with self._lock:
            logging.info("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.01)  # พอให้เห็นการแย่ง lock
            self.value = local_copy
            logging.info("Thread %s about to release lock", name)
        logging.info("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)

if __name__ == "__main__":
    format_str = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_str, level=logging.INFO, datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing locked update. Starting value is %d.", database.value)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # เรียง thread 0 ก่อน thread 1 เพื่อ log ออกมาเหมือนตัวอย่าง
        executor.submit(database.locked_update, 0)
        time.sleep(0.001)  # บังคับให้ thread 0 เริ่มก่อน thread 1 นิดหนึ่ง
        executor.submit(database.locked_update, 1)

    logging.info("Testing locked update. Ending value is %d.", database.value)