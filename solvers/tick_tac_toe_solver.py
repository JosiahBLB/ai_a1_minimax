from typing import List, Optional, Tuple
from solvers.solver_abc import Solver


class TicTacToeSolver(Solver):
    
    @classmethod
    def possible_actions(cls, state) -> List[List[int]]:
        """
        Returns a list of [row, col] elements
        """
        possible_moves = []
        for row in range(len(state)):
            possible_moves += [[row, col] for col in range(len(state)) if state[row][col] == " "]
        return possible_moves
    
    @classmethod
    def evaluate(cls, state) -> int:
        size = len(state)

        # Weighting of the evaluation function
        weight = [0]+[2**i for i in range(size)]

        # index of a list can be the occurances for the character 
        # e.g 2 occurances of X in only one row is list[2] = 1
        o_occurances = [0 for i in range(size+1)]
        x_occurances = [0 for i in range(size+1)]

        # find occurances of character:

        # rows
        for row in range(size):
            o_count = len([state[row][col] for col in range(size) if state[row][col] == "O"])
            o_occurances[o_count] += 1
            x_count = len([state[row][col] for col in range(size) if state[row][col] == "X"])
            x_occurances[x_count] += 1

        # columns
        for col in range(size):
            o_count = len([state[row][col] for row in range(size) if state[row][col] == "O"])
            o_occurances[o_count] += 1
            x_count = len([state[row][col] for row in range(size) if state[row][col] == "X"])
            x_occurances[x_count] += 1

        # diagonals
        o_count = len([state[i][i] for i in range(size) if state[i][i] == "O"])
        o_occurances[o_count] += 1
        x_count = len([state[i][i] for i in range(size) if state[i][i] == "X"])
        x_occurances[x_count] += 1

        o_count = len([state[i][size-i-1] for i in range(size) if state[i][size-i-1] == "O"])
        o_occurances[o_count] += 1
        x_count = len([state[i][size-i-1] for i in range(size) if state[i][size-i-1] == "X"])
        x_occurances[x_count] += 1

        # Evaluation fuction: eval = x_occurances * weights - o_occurances * weight
        weighted_x_vals = sum([vals*weights for vals, weights in zip(weight, x_occurances)])
        weighted_o_vals = sum([vals*weights for vals, weights in zip(weight, o_occurances)])

        evaluation = weighted_x_vals - weighted_o_vals

        return evaluation

    @classmethod
    def is_terminal(cls, state) -> bool:
        return (cls.check_win(state) != None)
    
    @classmethod
    def check_win(cls, state) -> Optional[str]:
        """
        Checks if either player has won the game.
        
        @param board - The 2d array of the current board state.
        @return str - The winning character e.g. 'X'
        """
        size = len(state)
        # Check rows
        for row in range(size):
            if all(state[row][col] == state[row][0] and state[row][0] != ' ' for col in range(size)):
                return state[row][0]
        # Check columns
        for col in range(size):
            if all(state[row][col] == state[0][col] and state[0][col] != ' ' for row in range(size)):
                return state[0][col]
        # Check diagonals
        if all(state[i][i] == state[0][0] and state[0][0] != ' ' for i in range(size)):
            return state[0][0]
        if all(state[i][size-i-1] == state[0][size-1] and state[0][size-1] != ' ' for i in range(size)):
            return state[0][size-1]
        # check draw
        no_spaces = []
        for row in range(size):
            no_spaces += [state[row][col] != " " for col in range(size)]
        if all(no_spaces):
            return "draw"
        # No winner
        return None
    
    @classmethod
    def next_player(cls, player) -> Tuple[str, bool]:
        return ('O', False) if player == 'X' else ('X', True)