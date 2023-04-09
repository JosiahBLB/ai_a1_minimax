from copy import deepcopy
from math import inf
from typing import Tuple
from solvers.solver_abc import Solver


class Node:
    def __init__(self, state: list, player: str, game: Solver) -> None:
        self.game = game
        self.state = state
        self.player = player
        self.move: list
        self.children = []

    def get_children(self) -> list: #: TODO: Debug: Evaluation returning nonetype
        player = self.game.next_player(self.player)
        moves = self.game.possible_actions(self.state)
        for move in moves:
            new_state = deepcopy(self.state)
            self.move = move
            new_state[move[0]][move[1]] = player
            self.children.append(Node(new_state, player, self.game))
        return self.children
    
    def evaluate(self) -> Tuple[int, list]: # Get the numerical value for the current state
        (self.game.evaluate(self.state), self.move)
    
    def is_terminal(self) -> bool: # Player has won or no more moves to play
        return self.game.is_terminal(self.state)

def minimax(node: Node, depth: int, maximizing_player: bool):
    max_val(node, depth, maximizing_player) if maximizing_player else min_val(node, depth, maximizing_player)
    
def max_val(node, depth, alpha = -inf, beta = inf):
    if (depth == 0 or node.is_terminal()):
        return node.evaluate()
    if (maximizing_player):
        value = -inf
        move = None
        for child in node.get_children():
            value2, move2 = max(value, minimax(child, depth - 1, False))
            if value2 > value:
                value = value2
                move = move2
        return value

def min_val(node, depth, alpha=-inf, beta=inf):
    if (depth == 0 or node.is_terminal()):
        return node.evaluate()
    value = inf
    move = None
    for child in node.get_children():
        value2, move2 = minimax(child, depth - 1, True)
        if value2 < value:
            value = value2
            move = move2
    return (value, move)