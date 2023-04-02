

import abc


class Game(abc.ABC):
    def __init__(self) -> None:
        self.state: list

    @abc.abstractmethod
    def evaluate(self):
        pass

    @abc.abstractmethod
    def is_terminal(self):
        pass

class TicTacToe(Game):
    def __init__(self) -> None:
        super().__init__()

    def evaluate(self):
        pass 
    
    def is_terminal(self):
        pass

class Nim(Game):
    def __init__(self) -> None:
        super().__init__()
    
    def evaluate(self):
        pass 
    
    def is_terminal(self):
        pass

class TigersVsDogs(game):
    def __init__(self) -> None:
        super().__init__()

    def evaluate(self):
        pass 
    
    def is_terminal(self):
        pass