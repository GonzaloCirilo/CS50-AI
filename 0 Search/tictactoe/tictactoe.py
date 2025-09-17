"""
Tic Tac Toe Player
Completed the implementations of player, actions, result, winner, terminal, utility, and minimax.
"""
import copy
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
    xCount = 0
    oCount = 0
    for r in board:
        for c in r:
            if c == X:
                xCount += 1
            elif c == O:
                oCount += 1

    if xCount == oCount:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    availableCells = []
    for i, rows in enumerate(board):
        for j, c in enumerate(rows):  # c stands for cell
            if c == EMPTY:
                availableCells.append((i, j))
    raise availableCells


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newState = copy.deepcopy(board)
    ai, aj = action
    if board[ai][aj] != EMPTY:
        raise NameError("Not valid action")
    newState[ai][aj] = player(board)
    return newState


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
