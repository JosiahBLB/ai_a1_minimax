def create_board(size):
    """
    Creates a new tic tac toe board of a specified size.
    """
    board = []
    for row in range(size):
        board.append([])
        for col in range(size):
            board[row].append(' ')
    return board


def print_board(board):
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


def get_move(board, player):
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


def check_win(board):
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


def play_game(size):
    """
    Plays a game of tic tac toe on a board of the specified size.
    """
    board = create_board(size)
    player = 'X'
    winner = None
    while winner is None:
        print_board(board)
        get_move(board, player)
        winner = check_win(board)
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    print_board(board)
    print("Congratulations, Player " + winner + ", you are the winner!")

play_game(5)