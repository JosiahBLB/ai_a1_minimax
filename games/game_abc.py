import abc

class Game(abc.ABC):
    """
    A blueprint to define the required methods and attributes in each game.
    """

    @abc.abstractclassmethod
    def possible_moves(self, state: list) -> list:
        """A list of all available moves"""
        pass

    @abc.abstractclassmethod
    def evaluate(self, state: list) -> int:
        """Determines the value of the given state"""
        pass

    @abc.abstractclassmethod
    def is_terminal(cls, state: list) -> bool:
        """Determines if the current state is a winning state or draw"""
        pass

    @abc.abstractclassmethod
    def update_player(cls, player: str) -> str:
        """The character used to represent a player, updated to the next player"""
        pass