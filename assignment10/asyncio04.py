import asyncio
from datetime import datetime

def ts() -> str:
    return datetime.now().strftime("%a %b %d %H:%M:%S %Y")

# ----- Producer -----
async def Producer(name: str, items: list[str], q: asyncio.Queue, idx: int):
    loop = asyncio.get_event_loop()
    arrival_clock = loop.time()
    arrival_time = ts()
    print(f"[{arrival_time}] ({idx}) {name} finished shopping: {items}")
    await q.put((idx, name, items, arrival_time, arrival_clock))

# ----- Consumer -----
async def cashier(cid: int, per_item_sec: float, q: asyncio.Queue):
    served = 0
    total_time = 0.0
    try:
        while True:
            idx, name, items, arrival_time, arrival_clock = await q.get()

            loop = asyncio.get_event_loop()
            start_clock = loop.time()
            start_time = ts()

            waiting_time = start_clock - arrival_clock  # <-- เวลารอคิว

            print(f"[{start_time}] [Cashier-{cid}] start {name} (#{idx}) "
                  f"(arrived {arrival_time}, waited {waiting_time:.2f} sec) "
                  f"with {items}")

            for _ in items:
                await asyncio.sleep(per_item_sec)

            finish_clock = loop.time()
            finish_time = ts()
            duration = finish_clock - start_clock

            served += 1
            total_time += duration

            print(f"[{finish_time}] [Cashier-{cid}] finished {name} (#{idx}) "
                  f">>>(took {duration:.2f} sec)<<<")

            q.task_done()

    except asyncio.CancelledError:
        print(f"[{ts()}] [Cashier-{cid}] closed (served {served} customers, "
              f"worked {total_time:.2f} sec total)")
        raise

# ----- Main -----
async def main():
    q = asyncio.Queue(maxsize=5)

    c1 = asyncio.create_task(cashier(1, 1, q))
    c2 = asyncio.create_task(cashier(2, 2, q))

    customers = [
        ("Alice",   ["Apple", "Banana", "Milk"]),
        ("Bob",     ["Bread", "Cheese"]),
        ("Charlie", ["Eggs", "Juice", "Butter"]),
        ("Diana",   ["Yogurt"]),
        ("Eve",     ["Cereal", "Coffee"]),
        ("Frank",   ["Tea", "Sugar", "Flour"]),
        ("Grace",   ["Chicken", "Rice"]), 
        ("Hank",    ["Fish", "Lemon", "Salt"]),
        ("Ivy",     ["Pasta", "Tomato Sauce"]),
        ("Jack",    ["Ice Cream"]),
    ]

    jobs = [
        Producer(name, items, q, idx+1)
        for idx, (name, items) in enumerate(customers)
    ]
    await asyncio.gather(*jobs)

    await q.join()

    for t in (c1, c2):
        t.cancel()
    await asyncio.gather(c1, c2, return_exceptions=True)

    print(f"[{ts()}] [Main] Supermarket closed!")

if __name__ == "__main__":
    asyncio.run(main())
