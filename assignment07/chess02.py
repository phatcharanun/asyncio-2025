import asyncio
from datetime import timedelta

speed = 100
Judit_time = 5 / speed
Opponent_time = 55 / speed
opponents = 24
move_pairs = 30

async def game(x):
    start = asyncio.get_event_loop().time()
    for i in range(move_pairs):
        await asyncio.sleep(Judit_time)
        print(f"BOARD-{x+1} {i+1} Judit made a move with {int(Judit_time * speed)} secs.")
        await asyncio.sleep(Opponent_time)
        print(f"BOARD-{x+1} {i+1} Opponent made move with {int(Opponent_time * speed)} secs.")
    
    elapsed = (asyncio.get_event_loop().time() - start) * speed
    print(f"BOARD-{x+1} - >>>>>>>>>>>>>>>>> Finished move in {elapsed:.1f} secs.")
    return elapsed

async def main():
    print(f"Number of games: {opponents} games.")
    print(f"Number of move: {move_pairs} pairs.\n")
    
    start = asyncio.get_event_loop().time()
    
    # Run all games simultaneously
    results = await asyncio.gather(*(game(i) for i in range(opponents)))

    max_elapsed = max(results)
    total_time = str(timedelta(seconds=round(max_elapsed)))

    print(f"\nBoard exhibition finished for {opponents} opponents in {total_time} hr.")

if __name__ == "__main__":
    asyncio.run(main())