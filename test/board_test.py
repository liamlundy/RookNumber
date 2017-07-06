import pytest

from rook_number.board import Board


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


@pytest.mark.skip("Equality not implemented")
def test_copy():
    board = Board(3, 3)
    board_copy = board.copy()
    assert board == board_copy

