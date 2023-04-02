size = 3
state = [["" for i in range(size)] for j in range(size)]
print(state)

def is_terminal(state: list):
    top_row = (state[0][0], state[0][1], state,[0][2])
    mid_row = (state[1][0], state[1][1], state,[1][2])
    bot_row = (state[2][0], state[2][1], state,[2][2])

    lef_col = (state[0][0], state[1][0], state,[2][0])
    mid_col = (state[0][1], state[1][1], state,[2][1])
    bot_col = (state[0][2], state[1][2], state,[2][2])

    diag_rgt = (state[0][0], state[1][1], state,[2][2])
    diag_lef = (state[2][0], state[1][1], state,[0][2])

    solutions = (top_row, mid_row, bot_row, lef_col, mid_col, bot_col, diag_rgt, diag_lef)
    