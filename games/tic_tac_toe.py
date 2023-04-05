import os
from typing import Optional
from games.game_abc import Game
from minimax import Node, minimax


class TicTacToe(Game):
    def __init__(self, size: int) -> None:
        self.play_game(size)
        super().__init__()
        self.size = size
        self.player = 'X'
    
    def possible_moves(self, state) -> list:
        """
        For use with minimax algorithum
        """
        possible_moves = []
        for row in range(self.size):
            possible_moves += [[row, col] for col in range(self.size) if state[row][col] == " "]
        return possible_moves
    
    def evaluate(self) -> int:
        board = self.state
        size = len(board)

        # Weighting of the evaluation function
        weight = [2**i for i in range(board)]

        # index of a list can be the occurances for the character 
        # e.g 2 occurances of X in only one row is list[2] = 1
        o_occurances = [0 for i in range(board)]
        x_occurances = [0 for i in range(board)]

        # find occurances of character:

        # rows
        for row in range(board):
            o_count = len([board[row][col] for col in range(size) if board[row][col] == "O"])
            o_occurances[o_count] += 1
            x_count = len([board[row][col] for col in range(size) if board[row][col] == "X"])
            x_occurances[x_count] += 1

        # columns
        for col in range(board):
            o_count = len([board[row][col] for row in range(size) if board[row][col] == "O"])
            o_occurances[o_count] += 1
            x_count = len([board[row][col] for row in range(size) if board[row][col] == "X"])
            x_occurances[x_count] += 1

        # diagonals
        o_count = len([board[i][i] for i in range(size) if board[i][i] == "O"])
        o_occurances[o_count] += 1
        x_count = len([board[i][i] for i in range(size) if board[i][i] == "X"])
        x_occurances[x_count] += 1

        o_count = len([board[i][size-i-1] for i in range(size) if board[i][size-i-1] == "O"])
        o_occurances[o_count] += 1
        x_count = len([board[i][size-i-1] for i in range(size) if board[i][size-i-1] == "X"])
        x_occurances[x_count] += 1

        # Evaluation fuction: eval = x_occurances * weights - o_occurances * weight
        weighted_x_vals = sum([vals*weights for vals, weights in zip(weight, x_occurances)])
        weighted_o_vals = sum([vals*weights for vals, weights in zip(weight, o_occurances)])

        evaluation = weighted_x_vals - weighted_o_vals

        return evaluation

    def is_terminal(self) -> bool:
        return (self.check_win() != None)

    @classmethod
    def create_board(cls, size: int) -> None:
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
    def get_move(cls, state: list, player: str) -> None:
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
    def update_player(cls, player) -> str:
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        return player

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
        # check draw
        no_spaces = []
        for row in range(size):
            no_spaces += [board[row][col] != " " for col in range(size)]
        if all(no_spaces):
            return "draw"
        # No winner
        return None

    def play_game(self, size) -> None:
        """
        Plays a game of tic tac toe on a board of the specified size.
        """
        board = self.create_board(size)
        winner = None
        player = self.player
        while winner is None: # Main loop

            self.print_board(board) 
            self.state = board # Save board in instance varible for minimax
            
            if player == "X":
                self.get_move(board, player) # Updates board and validation
            else:
                minimax(Node(board, player), 10, False)
            winner = self.check_win(board)
            player = self.update_player(player)

        # Game ends 
        os.system("cls")
        self.print_board(board)
        if winner == "draw":
            print("It's a draw! Better luck next time.")
        else:
            print("Congratulations, Player " + winner + ", you are the winner!")