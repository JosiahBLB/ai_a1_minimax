import abc

class Game(abc.ABC):
    """
    A blueprint to define the required methods and attributes in each game.
    """
    def __init__(self) -> None:
        self.state: list

    @abc.abstractmethod
    def possible_moves(self, state: list) -> list:
        pass

    @abc.abstractmethod
    def evaluate(self) -> int:
        pass

    @abc.abstractmethod
    def is_terminal(self) -> bool:
        pass
    
    @abc.abstractmethod
    def update_player(cls, player) -> str:
        pass