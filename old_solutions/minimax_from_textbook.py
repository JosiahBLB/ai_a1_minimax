from math import inf
from typing import Callable, Optional


class TwoPlayerGame():

    def __init__(self, depth) -> None:
        self.max_players_turn = False
        self.actions_set: list = []
        self.search_depth: int = depth

    def to_move(self) -> bool:
        return not self._max_players_turn

    def is_terminal(self) -> bool:
        """No avaliable moves or depth has been reached"""
        pass

    def utility(self) -> int:
        """Finds the value of the terminal state"""
        pass

    def eval_func(self, state, action) -> int:
        """Scores non-terminal states"""
        pass

    def actions(self) -> "list[Callable]":
        pass


class NaughtsAndCrosses(TwoPlayerGame):
    
    def __init__(self) -> None:
        pass

    def eval_func(self, state, action) -> int:
        pass

    def actions(self) -> list:
        pass
    
class State:

    def __init__(self) -> None:
        self.value: int # The value of the current node
        self.alpha: int
        self.beta: int
    

def alpha_beta_search(game: TwoPlayerGame, state: State) -> list:
    game.max_players_turn = game.to_move(state)
    state.value, move = max_value(game, state, -inf, inf)
    return move

def max_value(game: TwoPlayerGame, state, alpha, beta) -> "tuple[int, Callable]":
    # Check if at Terminal node
    if game.is_terminal(state):
        return (game.utility(state, game.max_players_turn), None)
    
    # Start recursive search
    value = -inf
    for action in game.actions(state):
        value_2, action_2 = min_value(game, game.eval_func(state, action), alpha, beta) # a2 is never used...?
        
        # Pruning
        if value_2 > value:
            value, move = value_2, action
            alpha = min(alpha, value)
        if value >= beta:
            return (value, move)
        return (value, move)
    
def min_value(game: TwoPlayerGame, state, alpha, beta) -> "tuple[int, Callable]":
    # Check if at Terminal node
    if game.is_terminal(state):
        return (game.utility(state, game.max_players_turn), None)
    
    # Start recursive search
    value = inf
    for action in game.actions(state):
        value_2, action_2 = min_value(game, game.eval_func(state, action), alpha, beta) # a2 is never used...?
        
        # Pruning
        if value_2 > value:
            value, move = value_2, action
            alpha = max(alpha, value)
        if value >= beta:
            return (value, move)
        return (value, move)
