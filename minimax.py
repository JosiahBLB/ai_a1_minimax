from math import inf
from games.game_abc import Game


class Node:
    def __init__(self, game: Game, player: str) -> None:
        self.game = game
        self.state: list
        self.player: str = self.game.update_player(player) # apon creation, players 

    def get_children(self) -> list: # The set of next possible moves
        moves = Game.possible_moves() # A list containing [row, col] items. These are possible moves
        children = []
        for move in moves: # Make a new child for each possible move
            new_state = self.state.copy
            new_state[move[0]][move[1]] = self.player # updating board with the new move
            children.append(Node(new_state, self.player)) # Adding new child node to the list. Passing board state and who's turn it is
        return children
    
    def evaluate(self) -> int: # Get the numerical value for the current state
        self.game.evaluate()
    
    def is_terminal(self) -> bool: # Player won or no more moves to play
        return self.game.is_terminal()

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
    root = Node()
    minimax(root, inf, True)