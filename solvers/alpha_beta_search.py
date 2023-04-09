from copy import deepcopy
from math import inf
from typing import List, Tuple
from solvers.solver_abc import Solver


class Node:
    def __init__(self, state:list, prev_player:str, solver:Solver, last_move:list = None) -> None:
        self.solver = solver
        self.state = state
        self.last_move: list = last_move
        self.player, self.max_players_turn = self.solver.next_player(prev_player)

    def possible_actions(self) -> list:
        """ List of possible actions, where each action is [int, int] representing coordinates """
        return self.solver.possible_actions(self.state)
    
    def evaluate(self) -> int: 
        """ Get the numerical value for the current state """
        return self.solver.evaluate(self.state)
    
    def is_terminal(self) -> bool:
        """ Player has won or no more moves to play """
        return self.solver.is_terminal(self.state)
    
def alpha_beta_search(node:Node) -> List[list]:
    """ vap = value action pair """
    value, action = max_val(node, -inf, inf) if(node.max_players_turn) else min_val(node, -inf, inf)
    return action

def max_val(node:Node, alpha:int, beta:int) -> Tuple[int, list]:
    if node.is_terminal():
        return node.evaluate(), node.last_move
    v = -inf
    for action in node.possible_actions():
        new_state = deepcopy(node.state)
        new_state[action[0]][action[1]] = node.player
        v2, a2 = min_val(Node(new_state, node.player, node.solver, action), alpha, beta)
        if v2 > v:
            v, a = v2, a2
            alpha = max(alpha, v)
        if v >= beta:
            return v, a
    return v, a
    
def min_val(node:Node, alpha:int, beta:int) -> Tuple[int, list]:
    if node.is_terminal():
        return node.evaluate(), node.last_move
    v = inf
    for action in node.possible_actions():
        new_state = deepcopy(node.state)
        new_state[action[0]][action[1]] = node.player
        v2, a2 = max_val(Node(new_state, node.player, node.solver, action), alpha, beta)
        if v2 < v:
            v, a = v2, a2
            beta = max(beta, v)
        if v <= alpha:
            return v, a
    return v, a