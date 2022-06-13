"""
Tic Tac Toe Player
"""

from copy import deepcopy
from json.encoder import INFINITY
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x, o = 0, 0
    for row in board:
        for col in row:
            if col == X:
                x += 1
            elif col == O:
                o += 1
    return X if x == o else O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not action:
        raise Exception("Invalid action!")
    i, j = action
    if not(i in range(3) and j in range(3)) or board[i][j] != EMPTY:
        raise Exception("Invalid action!")

    result = deepcopy(board)
    result[i][j] = player(board)
    return result

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != EMPTY:
        return board[0][0]
    return board[0][2] if board[0][2] == board[1][1] == board[2][0] and board[1][1] != EMPTY else None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 0 if not winner(board) else 1 if winner(board) == X else -1

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)
    next, next_action = -math.inf if current_player == X else math.inf, None

    for action in actions(board):
        val = optimum_value(result(board, action), -math.inf, math.inf)
        if current_player == X and val > next:
            next = val
            next_action = action
        elif current_player == O and val < next:
            next = val
            next_action = action

    return next_action

    raise NotImplementedError


def optimum_value(board, alpha, beta):
    current_player = player(board)
    next = -math.inf if current_player == X else math.inf

    for action in actions(board):
        new_board = result(board, action)
        if terminal(new_board):
            return utility(new_board)
        val = optimum_value(new_board, alpha, beta)
        if current_player == X:
            next = max(next, val)
            alpha = max(alpha, next)
            if beta <= alpha:
                break
        elif current_player == O:
            next = min(next, val)
            beta = min(beta, next)
            if beta <= alpha:
                break

    return next