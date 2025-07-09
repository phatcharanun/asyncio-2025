import asyncio
import time
from datetime import timedelta

speed = 10000  # speed
Judit_time = 5 / speed  # Judit time move
Opponent_time = 55 / speed  # Opponent time move
opponents = 24  # Number of opponents
move_pairs = 30  # Number of move pairs

async def game(x):
    board_start_time = time.perf_counter()
    calculated_board_start_time = 0

    for i in range(move_pairs):
        time.sleep(Judit_time)  # Still synchronous for Judit
        calculated_board_start_time += Judit_time
        print(f"BOARD-{x+1} {i+1} Judit made a move with {int(Judit_time * speed)} secs.")

    await asyncio.sleep(Opponent_time)
    print(f"BOARD-{x+1} {move_pairs} Opponent made move with {int(Opponent_time * speed)} secs.")
    calculated_board_start_time += Opponent_time

    actual_duration = (time.perf_counter() - board_start_time) * speed
    calculated_duration = calculated_board_start_time * speed

    #print(f"BOARD-{x+1} >>>>>>>>>>>>>>>>> Finished move in {actual_duration:.1f} secs")
    print(f"BOARD-{x+1} >>>>>>>>>>>>>>>>> Finished move in {calculated_duration:.1f} secs (calculated)\n")

    return {
        'board_time': actual_duration,
        'calculated_board_time': calculated_duration
    }

async def main():
    print(f"Number of games: {opponents} games.")
    print(f"Number of move: {move_pairs} pairs.\n")

    start_time = time.perf_counter()
    tasks = []

    for board in range(opponents):
        tasks.append(asyncio.create_task(game(board)))

    results = await asyncio.gather(*tasks)

    total_actual_time = sum(r['board_time'] for r in results)
    total_calculated_time = sum(r['calculated_board_time'] for r in results)

  #  print(f"Board exhibition finished for {opponents} opponents in {timedelta(seconds=round(total_actual_time))} hr.")
    print(f"Board exhibition finished for {opponents} opponents in {timedelta(seconds=round(total_calculated_time))} hr. (calculated)")
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")

if __name__ == "__main__":
    asyncio.run(main())
