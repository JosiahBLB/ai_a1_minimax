from solvers.solver_abc import Game


class TigersVsDogs(Game):
    def __init__(self) -> None:
        super().__init__()

    def evaluate(self):
        #
        pass 
    
    def is_terminal(self):
        #
        pass
    
    @classmethod
    def create_board(size):     
        board = [[" " for _ in range(size)] for _ in range(size)]
        board[2][2] = "T"
        board[0] = ["D"] * 5
        board[1][0], board[1][-1] = "D", "D"
        board[2][0], board[2][-1] = "D", "D"
        board[3][0], board[3][-1] = "D", "D"
        board[-1] = ["D"] * 5
        return board
    
    def print_board(board):
        for row in board:
            print("|".join(row))

    board = create_board(5)
    print_board(board)

# #Check if the move is valid 
# def is_valid_move(board, player, from_pos, to_pos):
#     # Check if the 'from_pos' cell contains the player's piece
#         if board[from_pos[0]][from_pos[1]] != player:
#         return False`

#     # Check if the 'to_pos' cell is empty
#     if board[to_pos[0]][to_pos[1]] != " ":
#         return False

#     # Check if the move is a capture move
#     dx = to_pos[0] - from_pos[0]
#     dy = to_pos[1] - from_pos[1]
#     if abs(dx) == 2 and abs(dy) == 2:
#         mid_x = (from_pos[0] + to_pos[0]) // 2
#         mid_y = (from_pos[1] + to_pos[1]) // 2
#         if board[mid_x][mid_y] != ("D" if player == "T" else "T"):
#             return False

#     # Check if the move is an adjacent move
#     if abs(dx) + abs(dy) != 1:
#         return False

#     return True
