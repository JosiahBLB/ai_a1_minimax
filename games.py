
import abc
import itertools
import os
from typing import Optional


class Game(abc.ABC):
    """
    A blueprint to define the required methods and attributes in each game.
    """
    # def __init__(self) -> None:
    #     self.state: list

    # @abc.abstractmethod
    # def evaluate(self):
    #     pass

    # @abc.abstractmethod
    # def is_terminal(self):
    #     pass

class TicTacToe(Game):
    def __init__(self, size) -> None:
        self.play_game(size)
        super().__init__()

    @classmethod
    def create_board(cls, size: int) -> list:
        """
        Creates a new empty tic-tac-toe board of a specified size.
        """
        board = []
        for row in range(size):
            board.append([])
            for col in range(size):
                board[row].append(' ')
        return board

    @classmethod
    def print_board(cls, board: list) -> None:
        """
        Prints the current state of the tic-tac-toe board.
        """
        os.system("cls")
        size = len(board)
        print('  ', end='')
        for col in range(size):
            print(col, end=' ')
        print()
        for row in range(size):
            print(row, end=' ')
            for col in range(size):
                if col == size-1:
                    print(board[row][col], end='')
                else:
                    print(board[row][col], end='|')
            print()
            if row < size - 1:
                print('  ', end='')
                for i in range(size*2-1): # Aligns horizontal lines
                    print('-', end='')
                print()

    @classmethod
    def get_move(cls, board: list, player: str) -> None:
        """
        Gets a move from the player and updates the board accordingly.
        Most of the code here is input validation.

        @param board - The 2d array of the current board state.
        @param player - The character the current player is playing as e.g. 'X'
        """
        size = len(board)
        valid_move = False
        while not valid_move:
            move = input("Player " + player + ", enter your move (row col): ")
            move = move.split()
            
            # Check if input format is correct
            if len(move) != 2:
                print("Invalid input. Please enter two numbers separated by a space.")
                continue
            row, col = move
            if not row.isdigit() or not col.isdigit():
                print("Invalid input. Please enter two numbers separated by a space.")
                continue

            # Check if row or column index is valid
            row, col = int(row), int(col)
            if row < 0 or row >= size or col < 0 or col >= size:
                print("Invalid move. Please enter a row and column within the board.")
                continue

            # Check if the given space is occupied
            if board[row][col] != ' ':
                print("That space is already taken. Please choose another.")
                continue
            valid_move = True
        board[row][col] = player

    @classmethod
    def check_win(cls, board) -> Optional[str]:
        """
        Checks if either player has won the game.
        
        @param board - The 2d array of the current board state.
        @return str - The winning character e.g. 'X'
        """
        size = len(board)
        # Check rows
        for row in range(size):
            if all(board[row][col] == board[row][0] and board[row][0] != ' ' for col in range(size)):
                return board[row][0]
        # Check columns
        for col in range(size):
            if all(board[row][col] == board[0][col] and board[0][col] != ' ' for row in range(size)):
                return board[0][col]
        # Check diagonals
        if all(board[i][i] == board[0][0] and board[0][0] != ' ' for i in range(size)):
            return board[0][0]
        if all(board[i][size-i-1] == board[0][size-1] and board[0][size-1] != ' ' for i in range(size)):
            return board[0][size-1]
        # No winner
        return None


    def play_game(self, size) -> None:
        """
        Plays a game of tic tac toe on a board of the specified size.
        """
        board = self.create_board(size)
        player = 'X'
        winner = None
        game_length = size * size
        turn_count = 0
        while winner is None: # Main loop
            self.print_board(board)
            self.get_move(board, player)
            winner = self.check_win(board)
            turn_count += 1
            if turn_count == game_length: # Check for draw
                winner = "draw"
            if player == 'X':
                player = 'O'
            else:
                player = 'X'

        # Game ends 
        os.system("cls")
        self.print_board(board)
        if winner == "draw":
            print("It's a draw! Better luck next time.")
        else:
            print("Congratulations, Player " + winner + ", you are the winner!")

class Nim(Game):
    def __init__(self, rows) -> None:
        self.play_nim(rows)
        super().__init__()
    
    def print_board(self, sticks) -> None:
        os.system("cls")
        for i, row in enumerate(sticks):
            row_index = str(i+1).rjust(3)
            print(f"Row {row_index}:" + f"{'| ' * row}".center(len(sticks)+len(str(i))+8)) # print and centre the sticks

    def play_nim(self, rows):
        # Set up the game
        sticks = [i+1  for i in range(rows)]
        print("Welcome to Nim! Here's the starting board:")
        self.print_board(sticks)

        # Play the game
        current_player = 1   # Player 1 goes first
        while True:
            print(f"Player {current_player}'s turn.")
            row, num_to_remove = self.get_move(sticks)
            sticks[row] -= num_to_remove
            print(f"Player {current_player} takes {num_to_remove} stick(s) from row {row+1}.")
            self.print_board(sticks)
            if self.is_game_over(sticks):
                print(f"Player {current_player} wins!")
                break
            current_player = 3 - current_player   # Switch player (1 -> 2, 2 -> 1)

    def get_move(self, sticks):
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

    def is_game_over(self, sticks):
        return all(stick == 0 for stick in sticks)

class TigersVsDogs(Game):
    def __init__(self) -> None:
        super().__init__()

    def evaluate(self):
        pass 
    
    def is_terminal(self):
        pass

if __name__ == "__main__":
    # game = TicTacToe(3)
    game2 = Nim(10)