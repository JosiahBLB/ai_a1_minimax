from math import inf
from games import TicTacToe, Game

class Node:
    def __init__(self, game) -> None:
        self.game: Game = game

    def get_children(self) -> list: # The set of next possible moves
        return self.children
    
    def evaluate(self) -> int: # Get the numerical value for the current state
        self.game.evaluate()
    
    def is_terminal(self) -> bool: # Player won or no more moves to play
        pass

def minimax(node: Node, depth: int, maximizing_player: bool):
    if (depth == 0 or node.is_terminal()):
        return node.evaluate()
    if (maximizing_player):
        value = -inf
        for child in node.get_children():
            value = max(value, minimax(child, depth - 1, False))
        return value
    else: # Minimizing player
        value = inf
        for child in node.get_children():
            value = min(value, minimax(child, depth - 1, True))
        return value
    
if __name__ == "__main__":
    origin = Node()
    minimax(TicTacToe(3), inf, True)