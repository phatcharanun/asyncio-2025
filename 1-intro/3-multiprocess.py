import time
import threading
from datetime import datetime

def make_burger(student_id):
    start_time = datetime.now()
    start_timestamp = time.time() 
    print(f"[{start_time.strftime('%H:%M:%S')}] เริ่มทำเบอร์เกอร์ให้นักเรียนคนที่ {student_id}")

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 1. ทอดเบอร์เกอร์... (นักเรียน {student_id})")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 2. ทอดไก่... (นักเรียน {student_id})")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 3. ใส่ผักและชีส... (นักเรียน {student_id})")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 4. ห่อเบอร์เกอร์... (นักเรียน {student_id})")
    time.sleep(5)

    end_time = datetime.now()
    end_timestamp = time.time()
    duration = end_timestamp - start_timestamp

    print(f"[{end_time.strftime('%H:%M:%S')}]  เสร็จแล้ว! เบอร์เกอร์ของนักเรียนคนที่ {student_id} | เริ่ม: {start_time.strftime('%H:%M:%S')} | เสร็จ: {end_time.strftime('%H:%M:%S')} | ใช้เวลา: {duration:.2f} วินาที")

def main():
    start = time.time()

    threads = []
    for i in range(1, 6): 
        t = threading.Thread(target=make_burger, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()
    print(f"[{datetime.now().strftime('%H:%M:%S')}] ⏱ รวมเวลาทั้งหมด: {end - start:.2f} วินาที")

if __name__ == "__main__":
    main()