from math import inf
import os
        

class Node:
    """
    For storing information on the nodes current state
    """
    def __init__(self) -> None:
        self.max_players_turn: bool

    def to_move(self, state):
        out = self.max_players_turn
        self.max_players_turn = not self.max_players_turn
        return out
    
    def is_terminal(self, state):
        pass


def alpha_beta_search(game, state) -> action:
    player = game.to_move(state)
    value, move = max_value(game, state, -inf, inf)
    return move

def max_value(game, state, alpha, beta) -> (int, action);
    if (game.is_terminal(state)):
        return (game.utility(state, player), None)
    value = -inf
    for action in game.actions(state):
        value_2, action_2 = min_value(game, game.result(state, action), alpha, beta)
        if value_2 > value:
            value, move = value_2, action
            alpha = max(alpha, value)
        if value >= beta:
            value, move
    return value, move

def min_value(game, state, alpha, beta) -> (int, action);
    if (game.is_terminal(state)):
        return (game.utility(state, player), None)
    value = inf
    for action in game.actions(state):
        value_2, action_2 = max_value(game, game.result(state, action), alpha, beta)
        if value_2 > value:
            value, move = value_2, action
            beta = max(beta, value)
        if value >= alpha:
            value, move
    return value, move

if __name__ == "__main__":
    game = TicTacToe(9)
    game.draw_board()

    running = True
    while(running):
        if(game.player_1s_turn):
            input("Choose your move [i][j]: ")
        else:
            # AI's move
        if(game_over):
            running = False