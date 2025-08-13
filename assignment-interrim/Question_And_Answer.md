# Question
1. ถ้าสร้าง asyncio.create_task(*tasks) ที่ไม่มี await ที่ main() เกิดอะไรบ้าง
   1. งานบางส่วนอาจไม่รันเลย หรือรันไม่จบ เพราะ event loop ปิดไป
   2. ไม่มีการดักจับ exception ของ task error ใน task 
   3. งานบางส่วนอาจไม่รันเลย หรือรันไม่จบ เพราะ event loop ปิดไป
2. ความแตกต่างระหว่าง asyncio.gather(*tasks) กับ asyncio.wait(tasks) คืออะไร
   1. gather รวบรวมผลลัพธ์ของทุก task (return เป็น list ตามลำดับ input)
   2. wait() → คืนค่าเป็น (done, pending) set ของ task และไม่ได้รวมผลลัพธ์ให้ ต้องไปดึงเองจากแต่ละ task
   3. ..
3. สร้าง create_task() และ coroutine ของ http ให้อะไรต่างกัน
   1. สร้าง task เพื่อรัน coroutine ในพื้นหลังโดยไม่รอให้เสร็จ สามารถรันหลาย HTTP requests พร้อมกันได้
   2.Task สามารถเก็บ reference และรันไปเรื่อย ๆ ในขณะที่ coroutine ปกติจะรอจนเสร็จก่อนถึงทำอย่างอื่น
   3. การสร้าง task หลายตัว แล้วใช้ gather() หรือ wait() จะทำให้หลาย HTTP request ถูกส่งพร้อมกัน (parallel I/O) เร็วกว่าการรอทีละ request
