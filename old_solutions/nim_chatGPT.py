import random

def play_nim():
    # Set up the game
    rows = int(input("Enter the number of rows you want to play with: "))
    sticks = [i+1  for i in range(rows)]   # Randomly choose the number of sticks in each row
    print("Welcome to Nim! Here's the starting board:")
    print_board(sticks)

    # Play the game
    current_player = 1   # Player 1 goes first
    while True:
        print(f"Player {current_player}'s turn.")
        row, num_to_remove = get_move(sticks)
        sticks[row] -= num_to_remove
        print(f"Player {current_player} takes {num_to_remove} stick(s) from row {row+1}.")
        print_board(sticks)
        if is_game_over(sticks):
            print(f"Player {current_player} wins!")
            break
        current_player = 3 - current_player   # Switch player (1 -> 2, 2 -> 1)

def print_board(sticks):
    for i, row in enumerate(sticks):
        print(f"Row {i+1}:" + f"{'| ' * row}".center(len(sticks)+6))

def get_move(sticks):
    while True:
        row = int(input("Enter the row you want to take sticks from: ")) - 1   # Subtract 1 to convert to 0-indexed
        if row < 0 or row >= len(sticks):
            print(f"Invalid row. Please enter a number between 1 and {len(sticks)}.")
            continue
        if sticks[row] == 0:
            print(f"There are no sticks in row {row+1}. Please choose a different row.")
            continue
        num_to_remove = int(input(f"Enter the number of sticks you want to take from row {row+1}: "))
        if num_to_remove < 1 or num_to_remove > sticks[row]:
            print(f"Invalid number of sticks. Please enter a number between 1 and {sticks[row]}.")
            continue
        return row, num_to_remove

def is_game_over(sticks):
    return all(stick == 0 for stick in sticks)