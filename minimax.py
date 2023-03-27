from math import inf
from typing import Callable, Optional


class TwoPlayerGame():
    MAX_PLAYER = True
    MIN_PLAYER = False
    player: Optional[bool]

    def __init__(self, depth) -> None:
        self._max_players_turn = False
        self.actions_set: list = []
        self.search_depth: int = depth

    def to_move(self) -> bool:
        self._max_players_turn = not self._max_players_turn
        return self._max_players_turn

    def is_terminal(self) -> bool:
        """TwoPlayerGame has ended or depth has been reached"""
        pass

    def utility(self) -> int:
        """Assigning a number to a node"""
        pass

    def eval_func(self, state, action) -> int: # 
        """For evalutating terminal states"""
        pass

    def actions(self) -> "list[Callable]":
        pass


class NaughtsAndCrosses(TwoPlayerGame):
    
    def __init__(self) -> None:
        pass

    def eval_func(self, state, action) -> int: # For evalutating terminal states
        pass

    def actions(self) -> list:
        pass
    
class State:

    def __init__(self) -> None:
        self.value: int # The value of the current node
        self.alpha: int
        self.beta: int
    

def alpha_beta_search(game: TwoPlayerGame, state: State) -> list:
    TwoPlayerGame.player = game.to_move(state)
    state.value, move = max_value(game, state, -inf, inf)
    return move

def max_value(game: TwoPlayerGame, state, alpha, beta) -> "tuple[int, Callable]":
    # Check if at Terminal node
    if game.is_terminal(state):
        return (game.utility(state, TwoPlayerGame.player), None)
    
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
        return (game.utility(state, TwoPlayerGame.player), None)
    
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
