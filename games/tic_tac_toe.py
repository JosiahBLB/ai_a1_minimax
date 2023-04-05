import os
from typing import Optional
from games.game_abc import Game
from minimax import Node, minimax


class TicTacToe(Game):
    def __init__(self, size: int) -> None:
        self.play_game(size)
    
    """-------- Node Functions --------"""

    @classmethod
    def possible_moves(cls, state) -> list:
        """
        Returns a list of [row, col] elements
        """
        possible_moves = []
        for row in range(len(state)):
            possible_moves += [[row, col] for col in range(len(state)) if state[row][col] == " "]
        return possible_moves
    
    @classmethod
    def evaluate(cls, state) -> int:
        size = len(state)

        # Weighting of the evaluation function
        weight = [2**i for i in range(state)]

        # index of a list can be the occurances for the character 
        # e.g 2 occurances of X in only one row is list[2] = 1
        o_occurances = [0 for i in range(state)]
        x_occurances = [0 for i in range(state)]

        # find occurances of character:

        # rows
        for row in range(state):
            o_count = len([state[row][col] for col in range(size) if state[row][col] == "O"])
            o_occurances[o_count] += 1
            x_count = len([state[row][col] for col in range(size) if state[row][col] == "X"])
            x_occurances[x_count] += 1

        # columns
        for col in range(state):
            o_count = len([state[row][col] for row in range(size) if state[row][col] == "O"])
            o_occurances[o_count] += 1
            x_count = len([state[row][col] for row in range(size) if state[row][col] == "X"])
            x_occurances[x_count] += 1

        # diagonals
        o_count = len([state[i][i] for i in range(size) if state[i][i] == "O"])
        o_occurances[o_count] += 1
        x_count = len([state[i][i] for i in range(size) if state[i][i] == "X"])
        x_occurances[x_count] += 1

        o_count = len([state[i][size-i-1] for i in range(size) if state[i][size-i-1] == "O"])
        o_occurances[o_count] += 1
        x_count = len([state[i][size-i-1] for i in range(size) if state[i][size-i-1] == "X"])
        x_occurances[x_count] += 1

        # Evaluation fuction: eval = x_occurances * weights - o_occurances * weight
        weighted_x_vals = sum([vals*weights for vals, weights in zip(weight, x_occurances)])
        weighted_o_vals = sum([vals*weights for vals, weights in zip(weight, o_occurances)])

        evaluation = weighted_x_vals - weighted_o_vals

        return evaluation

    @classmethod
    def is_terminal(cls, state) -> bool:
        return (cls.check_win(state) != None)
    
    @classmethod
    def update_player(cls, player) -> str:
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        return player

    """-------- Game Functions --------"""

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

    def play_game(self, size) -> None:
        """
        Plays a game of tic tac toe on a board of the specified size.
        """
        state = self.create_board(size)
        winner = None
        player = "X"
        while winner is None: # Main loop
            self.print_board(state) 
            if player == "X":
                self.get_move_from_user(state, player) # Updates board and validation
            else:
                minimax(Node(state, player, TicTacToe), 10, False)
            winner = self.check_win(state)
            player = self.update_player(player)

        # Game ends 
        os.system("cls")
        self.print_board(state)
        if winner == "draw":
            print("It's a draw! Better luck next time.")
        else:
            print("Congratulations, Player " + winner + ", you are the winner!")