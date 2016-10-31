import pytest
from board import Board, RooksBoard


class TestBoard:

    def test_empty_board(self):
        with pytest.raises(AssertionError):
            Board(0, 0)

    def test_set_cell(self):
        board = Board(3, 3)
        board.set_cell(1, 1, True)
        assert board.get_cell(1, 1)

    def test_outside_index(self):
        board = Board(3, 3)
        with pytest.raises(IndexError):
            board.get_cell(3, 0)
        with pytest.raises(IndexError):
            board.get_cell(0, 3)

    @pytest.mark.skip("Equality not implemented")
    def test_copy(self):
        board = Board(3, 3)
        board_copy = board.copy()
        assert board == board_copy


class TestRookBoard:

    def test(self):
        assert True

