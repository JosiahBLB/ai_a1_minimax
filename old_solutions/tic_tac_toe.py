
import itertools
import os


class TicTacToe:
    """
    For storing game specific rules or states
    """
    PLAYER_1 = "X"
    PLAYER_2 = "O"

    def __init__(self, size) -> None:
        self.board = [[" " for _ in range(size)] for __ in range(size)] # Initialse an empty board
        self.player_1s_turn: bool = True
        self.size = size
        
    def draw_board(self):
        # A single method to print out the current board.
        os.system("cls")
        size = len(self.board)
        for i in range(size):
            if(i != 0 and i != size):
                print("-"*((size*2)-1))
            for j in range(size):
                if(j != (size-1)):
                    print(self.board[i][j]+"|", end="")
                else:
                    print(self.board[i][j])

    def to_move(self):
        pass

    def is_terminal(self):
        # Dynamically stores all of the solutions to any n x n sized board, given that a solution will be n long.
        # Might be a pointless game, but no need to make this harder than it needs to be.

        possible_solutions = [itertools.chain([[self.board[i][j] for j in range(self.size)] for i in range(self.size)]), # Rows
                              itertools.chain([[self.board[i][j] for i in range(self.size)] for j in range(self.size)]), # Columns
                              [self.board[i][i] for i in range(self.size)], # \ Diagonal left to right -> top to bottom
                              [self.board[-i][-i] for i in range(self.size)]] # / Diagonal left to right -> bottom to top
        
        players = [TicTacToe.PLAYER_1, TicTacToe.PLAYER_2]
        solution = [[player for _ in range(self.size)] for player in players] # Array of X's or O's e.g. [X, X, X, ... , X]

        if solution in possible_solutions: # TODO: needs work, how to determine who won?
            return True
        return False
    
if __name__ == "__main__":
    game = TicTacToe(9)
    
    running = True
    while(running):
        game.draw_board()
        if(game.player_1s_turn):
            p1_i = int(input("Player 1, choose a row: "))
            p1_j = int(input("Player 1, choose a column: "))
            game.board[p1_i][p1_j] = game.PLAYER_1

        else:
            p2_i = int(input("Player 2, choose a row: "))
            p2_j = int(input("Player 2, choose a column: "))
            game.board[p2_i][p2_j] = game.PLAYER_2

        if(game.is_terminal):
            running = False
    