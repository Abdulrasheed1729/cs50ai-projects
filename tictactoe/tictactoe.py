"""
Tic Tac Toe Player
"""

import math
import copy

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
    start = initial_state()
    if board == start:
        return X
    
    xlen = 0
    olen = 0
    for row in board:
        for tile in row:
            if tile == X:
                xlen += 1
            if tile == O:
                olen += 1
    if xlen > olen:
        return O
    if xlen <= olen:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is EMPTY:
                actions.add((i,j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    actions_list = actions(board)

    if action not in actions_list:
        raise Exception("invalid action")
    (i, j) = action

    result_board = copy.deepcopy(board)

    player_turn = player(board)

    result_board[i][j] = player_turn
    
    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    res = set()

    for i in range(len(board)):
        res = set(board[i])
        if len(res) == 1:
            res = list(res)
            if None in res:
                continue
            return res[0]
        res = set()
    
    res = set()
    
    for i in range(len(board)):
        res.add(board[i][i])

    if len(res) == 1:
        res = list(res)
        return list(res)[0]
    
    res = set()

    for i in range(len(board)):
        for j in range(len(board)):
            res.add(board[j][i])
        if len(res) == 1:
            res = list(res)
            return res[0]
        res = set()

    res = set()

    j = len(board) - 1
    for i in range(len(board)):
        res.add(board[i][j])
        j -= 1

    if len(res) == 1:
        res = list(res)
        return res[0]
    
    res = set()

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True
    
    for i in range(len(board)):
        if EMPTY in board[i]:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    is_terminal = terminal(board)

    if is_terminal:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    else: 
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None
    
    v = float('-inf')

    move = None

    for action in actions(board):
        aux, act = min_value(result(board, action))

        if aux > v:
            v = aux
            move = action

            if v == 1:
                return v, move
    
    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None
    
    v = float('inf')

    move = None

    for action in actions(board):
        aux, act = max_value(result(board, action))

        if aux < v:
            v = aux
            move = action

            if v == -1:
                return v, move
    
    return v, move

