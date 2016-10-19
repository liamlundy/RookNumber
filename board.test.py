import unittest
from board import Board, RooksBoard


class TestBoard(unittest.TestCase):

    def test_empty_board(self):
        self.assertRaises(AssertionError, Board, 0, 0)

    def test_set_cell(self):
        board = Board(3, 3)
        board.set_cell(1, 1, True)
        self.assertTrue(board.get_cell(1, 1))

    def test_outside_index(self):
        board = Board(3, 3)
        self.assertRaises(IndexError, board.get_cell, 3, 0)
        self.assertRaises(IndexError, board.get_cell, 0, 3)

    @unittest.skip("Equality not implemented")
    def test_copy(self):
        board = Board(3, 3)
        board_copy = board.copy()
        self.assertEqual(board, board_copy)


class TestRookBoard(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()