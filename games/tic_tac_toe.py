import os
from typing import Optional, Tuple
from solvers.alpha_beta_search import Node, alpha_beta_search
from solvers.tick_tac_toe_solver import TicTacToeSolver

class TicTacToe():
    def __init__(self) -> None:
        size, n_computers = self.game_init()
        self.play_game(size, n_computers)

    def game_init(self) -> Tuple[int, int]:
        valid_input = False
        while not valid_input:
            n_computers = input("Enter the number of computer players (max 2):")
            if len(n_computers) != 1:
                print("Please enter a valid number 0 to 2")
                continue
            if not n_computers.isdigit():
                print("Please enter a number")
                continue
            n_computers = int(n_computers)
            if n_computers < 0 and n_computers > 2:
                print("Please enter a valid number 0 to 2")
                continue
            valid_input = True
        
        valid_input = False
        while not valid_input:
            size = input("Enter the board size (n): ")
            if not size.isdigit():
                print("Please enter a single number")
                continue
            size = int(size)
            if size < 1:
                print("Please enter a number greater than 0")
                continue
            valid_input = True

        return size, n_computers

    def create_board(self, size: int) -> list:
        """
        Creates a new empty tic-tac-toe board of a specified size.
        """
        board = []
        for row in range(size):
            board.append([])
            for col in range(size):
                board[row].append(' ')
        return board

    def print_board(self, state: list) -> None:
        """
        Prints the current state of the tic-tac-toe board.
        """
        os.system("cls")
        size = len(state)
        print('  ', end='')
        for col in range(size):
            print(col, end=' ')
        print()
        for row in range(size):
            print(row, end=' ')
            for col in range(size):
                if col == size-1:
                    print(state[row][col], end='')
                else:
                    print(state[row][col], end='|')
            print()
            if row < size - 1:
                print('  ', end='')
                for i in range(size*2-1): # Aligns horizontal lines
                    print('-', end='')
                print()

    def get_move_from_user(self, state: list, player: str) -> None:
        """
        Gets a move from the player and updates the board accordingly.
        Most of the code here is input validation.

        @param board - The 2d array of the current board state.
        @param player - The character the current player is playing as e.g. 'X'
        """
        size = len(state)
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
            if state[row][col] != ' ':
                print("That space is already taken. Please choose another.")
                continue
            valid_move = True
        state[row][col] = player

    @classmethod
    def check_win(cls, state) -> Optional[str]:
        """
        Checks if either player has won the game.
        
        @param board - The 2d array of the current board state.
        @return str - The winning character e.g. 'X'
        """
        size = len(state)
        # Check rows
        for row in range(size):
            if all(state[row][col] == state[row][0] and state[row][0] != ' ' for col in range(size)):
                return state[row][0]
        # Check columns
        for col in range(size):
            if all(state[row][col] == state[0][col] and state[0][col] != ' ' for row in range(size)):
                return state[0][col]
        # Check diagonals
        if all(state[i][i] == state[0][0] and state[0][0] != ' ' for i in range(size)):
            return state[0][0]
        if all(state[i][size-i-1] == state[0][size-1] and state[0][size-1] != ' ' for i in range(size)):
            return state[0][size-1]
        # check draw
        no_spaces = []
        for row in range(size):
            no_spaces += [state[row][col] != " " for col in range(size)]
        if all(no_spaces):
            return "draw"
        # No winner
        return None

    def play_game(self, size, n_computers) -> None:
        """
        Plays a game of tic tac toe on a board of the specified size.
        """
        state = self.create_board(size)
        winner = None
        player = "X"
        while winner is None: # Main loop
            self.print_board(state)
            if n_computers == 2:
                    action = alpha_beta_search(Node(state, player, TicTacToeSolver))
                    state[action[0]][action[1]] = player
            elif n_computers == 1:
                if player == "X":
                    self.get_move_from_user(state, player)
                else:
                    action =  alpha_beta_search(Node(state, "X", TicTacToeSolver))
                    state[action[0]][action[1]] = player
            else:
                self.get_move_from_user(state, player)
            winner = self.check_win(state)
            if player == 'X':
                player = 'O'
            else:
                player = 'X'

        # Game ends 
        os.system("cls")
        self.print_board(state)
        if winner == "draw":
            print("It's a draw! Better luck next time.")
        else:
            print("Congratulations, Player " + winner + ", you are the winner!")