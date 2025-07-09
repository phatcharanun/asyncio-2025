import time  
from datetime import timedelta  
  
speed = 10000  # speed  
Judit_time = 5/speed  # Judit time move  
Opponent_time = 55/speed # Opponent time move  
opponents = 24 # Number of opponnents  
move_pairs = 30 # Number of move pairs  
  
def game(x):  
    # Loops {move_pairs} times to simulate both players making a move  
    board_start_time = time.perf_counter()  
    calculated_board_start_time = 0  
    for i in range(move_pairs):  
        time.sleep(Judit_time)  
        calculated_board_start_time = calculated_board_start_time + Judit_time  
        print(f"BOARD-{x+1} {i+1} Judit made a move with {int(Judit_time*speed)} secs.")  
  
    # The opponent thinks for 5 seconds.  
    time.sleep(Opponent_time)  
    print(f"BOARD-{x+1} {i+1} Opponent made move with {int(Opponent_time*speed)} secs.")  
    calculated_board_start_time = calculated_board_start_time + Opponent_time  
    print(f"BOARD-{x+1} >>>>>>>>>>>>>>>>> Finished move in {(time.perf_counter() - board_start_time)*speed:.1f} secs")  
    print(f"BOARD-{x+1} >>>>>>>>>>>>>>>>> Finished move in {calculated_board_start_time*speed:.1f} secs (calculated)\n")  
    return {  
        'board_time': (time.perf_counter() - board_start_time)*speed,  
        'calculated_board_time': calculated_board_start_time*speed  
    }  
  
if __name__ == "__main__":  
    print(f"Number of games: {opponents} games.")  
    print(f"Number of move: {move_pairs} pairs.")  
    start_time = time.perf_counter()  
    # Loops 24 times because we are playing 24 opponents.  
    boards_time = 0  
    calculated_board_time = 0  
    for board in range(opponents):  
        result = game(board)  
        boards_time += result['board_time']  
        calculated_board_time += result['calculated_board_time']  
  
    print(f"Board exhibition finished for {opponents} opponents in {timedelta(seconds=round(boards_time))} hr.")  
    print(f"Board exhibition finished for {opponents} opponents in {timedelta(seconds=round(calculated_board_time))} hr. (calculated)")  
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")  
