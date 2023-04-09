import abc
from typing import Tuple

class Solver(abc.ABC):
    """
    A blueprint to define the required methods and attributes in each game.
    """

    @abc.abstractclassmethod
    def possible_actions(cls, state: list) -> list:
        """A list of all available moves"""
        pass

    @abc.abstractclassmethod
    def evaluate(cls, state: list) -> int:
        """Determines the value of the given state"""
        pass

    @abc.abstractclassmethod
    def is_terminal(cls, state: list) -> bool:
        """Determines if the current state is a winning state or draw"""
        pass

    @abc.abstractclassmethod
    def next_player(cls, player: str) -> Tuple[str, bool]:
        """The character used to represent a player, updated to the next player"""
        pass