import pytest

from rook_number.board import Board, Row


def test_print_row():
    row = Row(3)
    row.set_cell(0, 1)
    row.set_cell(1, 'a')
    assert str(row) == '|x|x| |'


def test_row_equality():
    row1 = Row(4)
    row2 = Row(4)
    assert row1 == row2


def test_print_board():
    board = Board(3, 4)
    board.set_cell(2, 3, True)
    assert str(board) == '| | | | |\n| | | | |\n| | | |x|'


def test_empty_board():
    with pytest.raises(AssertionError):
        Board(0, 0)


def test_set_cell():
    board = Board(3, 3)
    board.set_cell(1, 1, True)
    assert board.get_cell(1, 1)


def test_outside_index():
    board = Board(3, 3)
    with pytest.raises(IndexError):
        board.get_cell(3, 0)
    with pytest.raises(IndexError):
        board.get_cell(0, 3)


def test_copy():
    board = Board(3, 3)
    board_copy = board.copy()
    assert board == board_copy

