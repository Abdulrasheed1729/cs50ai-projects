import pytest

from tictactoe import EMPTY, O, X
from tictactoe import player, actions, winner, result, terminal

empty_board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

x_turn_board = [[O, X, EMPTY],
                [O, EMPTY, X],
                [EMPTY, X, O]]

possible_turns_board = [[O, X, EMPTY],
                        [O, EMPTY, X],
                        [EMPTY, X, O]]

result_board = [[O, X, EMPTY],
                [O, EMPTY, X],
                [X, X, O]]

xwinner_board = [[O, X, EMPTY],
                [O, X, O],
                [EMPTY, X, O]]

o_winner_board = [[EMPTY, X, O],
                  [X, O, X],
                  [O, EMPTY, EMPTY]]

o_horizontal_winner_board = [[O, O, O],
                             [EMPTY, X, X],
                             [EMPTY, X, EMPTY]]

x_horizontal_winner_board = [[X, X, X],
                             [EMPTY, O, O],
                             [EMPTY, EMPTY, EMPTY]]

o_turn_board = [[X, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

tied_board = [[O, X, O],
              [X, O, X],
              [X, O, X]]

def test_player():
    assert player(empty_board) == X
    assert player(o_turn_board) == O
    assert player(x_turn_board) == X

def test_actions():
    assert actions(possible_turns_board) == {(0,2), (1,1), (2,0)}

def test_result():
    assert result(possible_turns_board, (2,0)) == result_board

def test_winner():
    assert winner(empty_board) is None
    assert winner(result_board) is None
    assert winner(xwinner_board) == X
    assert winner(o_winner_board) == O
    assert winner(o_horizontal_winner_board) == O
    assert winner(x_horizontal_winner_board) == X

def test_terminal():
    assert terminal(xwinner_board) == True
    assert terminal(o_winner_board) == True
    assert terminal(tied_board) == True
    

def test_me():
    res = set()
    res.add(None)
    res.add(5)
    assert len(res) == 2
