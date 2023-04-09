from solvers.solver_abc import Solver


class NimSolver(Solver):

    @classmethod
    def possible_actions(cls, state: list) -> list:
        """A list of all available moves"""
        pass

    @classmethod
    def evaluate(cls, state: list) -> int:
        """Determines the value of the given state"""
        pass

    @classmethod
    def is_terminal(cls, state: list) -> bool:
        """Determines if the current state is a winning state or draw"""
        pass

    @classmethod
    def next_player(cls, player: str) -> str:
        """The character used to represent a player, updated to the next player"""
        pass
