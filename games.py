
import abc


class Game(abc.ABC):
    """
    A blueprint to define the required methods and attributes in each game.
    """
    def __init__(self) -> None:
        self.state: list

    @abc.abstractmethod
    def evaluate(self):
        pass

    @abc.abstractmethod
    def is_terminal(self):
        pass

class TicTacToe(Game):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def create_board(cls, size):
        """
        Creates a new tic tac toe board of a specified size.
        """
        board = []
        for row in range(size):
            board.append([])
            for col in range(size):
                board[row].append(' ')
        return board

    @classmethod
    def print_board(cls, board):
        """
        Prints the current state of the tic tac toe board.
        """
        size = len(board)
        print('  ', end='')
        for col in range(size):
            print(col, end=' ')
        print()
        for row in range(size):
            print(row, end=' ')
            for col in range(size):
                print(board[row][col], end='|')
            print()
            if row < size - 1:
                print(' ', end='')
                for i in range(size):
                    print('-', end='')
                print()

    @classmethod
    def get_move(cls, board, player):
        """
        Gets a move from the player and updates the board accordingly.
        """
        size = len(board)
        valid_move = False
        while not valid_move:
            move = input("Player " + player + ", enter your move (row col): ")
            move = move.split()
            if len(move) != 2:
                print("Invalid input. Please enter two numbers separated by a space.")
                continue
            row, col = move
            if not row.isdigit() or not col.isdigit():
                print("Invalid input. Please enter two numbers separated by a space.")
                continue
            row, col = int(row), int(col)
            if row < 0 or row >= size or col < 0 or col >= size:
                print("Invalid move. Please enter a row and column within the board.")
                continue
            if board[row][col] != ' ':
                print("That space is already taken. Please choose another.")
                continue
            valid_move = True
        board[row][col] = player

    @classmethod
    def check_win(cls, board):
        """
        Checks if either player has won the game.
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


    def play_game(self, size):
        """
        Plays a game of tic tac toe on a board of the specified size.
        """
        board = self.create_board(size)
        player = 'X'
        winner = None
        while winner is None:
            self.print_board(board)
            self.get_move(board, player)
            winner = self.check_win(board)
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        self.print_board(board)
        print("Congratulations, Player " + winner + ", you are the winner!")

class Nim(Game):
    def __init__(self) -> None:
        super().__init__()
    
    def print_board(self, sticks) -> None:
        for i, row in enumerate(sticks):
            print(f"Row {i+1}:" + f"{'| ' * row}".center(len(sticks)+6))

    def play_nim(self):
        # Set up the game
        rows = int(input("Enter the number of rows you want to play with: "))
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

class TigersVsDogs(game):
    def __init__(self) -> None:
        super().__init__()

    def evaluate(self):
        pass 
    
    def is_terminal(self):
        pass