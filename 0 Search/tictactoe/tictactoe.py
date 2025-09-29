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
    return availableCells


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
    Creating an array to helps check every row, column a diagonal
    if sum is 3 then X wins, likewise if sum is -3 O wins else None
    """
    checks = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)]
    ]
    for check in checks:
        sum = 0
        for (i, j) in check:
            if board[i][j] == X:
                sum += 1
            elif board[i][j] == O:
                sum -= 1
        if sum == 3:
            return X
        elif sum == -3:
            return O

    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    Counting every non empty cell. If there is a winner or all cells are counted then we have a terminal state
    """
    count = 0
    for r in board:
        for c in r:
            if c != EMPTY:
                count += 1
    return winner(board) != EMPTY or count == 9


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerResult = winner(board)
    if winnerResult == X:
        return 1
    elif winnerResult == O:
        return -1
    else:
        return 0


def maximize(board):
    if terminal(board):
        return (utility(board), -1, -1)
    possibleMoves = actions(board)
    value = -1e9
    r = -1
    c = -1
    for (i, j) in possibleMoves:
        newBoard = result(board, (i, j))
        eval = minimize(newBoard)[0]
        if value < eval:
            r = i
            c = j
        value = max(eval, value)
    return (value, r, c)


def minimize(board):
    if terminal(board):
        return (utility(board), 0, 0)
    possibleMoves = actions(board)
    value = 1e9
    r = -1
    c = -1
    for (i, j) in possibleMoves:
        newBoard = result(board, (i, j))
        eval = maximize(newBoard)[0]
        if eval < value:
            r = i
            c = j
        value = min(eval, value)
    return (value, r, c)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return EMPTY
    # Values for alpha beta prunning
    alpha = -1e9
    beta = 1e9

    # Get if AI moves as X or O
    moveToken = player(board)

    # If playing as X AI should we should start maximizing, otherwise we use O and minize,
    if moveToken == X:
        result = maximize(board)
        return (result[1], result[2])
    else:
        result = minimize(board)
        return (result[1], result[2])
