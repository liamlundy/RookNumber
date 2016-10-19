from board import RooksBoard


class SimulationWithKRooks:
    def __init__(self, display=True):
        self.display = display
        self.count = 0

    def place_in_row(self, board, row_idx):
        try:
            if row_idx < board.num_rows:
                row = board.rows[row_idx]
                for col_idx, cell in enumerate(row.row):
                    if board.is_valid(row_idx, col_idx):
                        board_copy = board.copy()
                        board_copy.add_rook(row_idx, col_idx)
                        self.place_in_row(board_copy, row_idx + 1)
                self.place_in_row(board, row_idx + 1) # Maybe make copy first
            else:
                self.count += 1
                if self.display:
                    print("Board number: {}".format(self.count))
                    print(board)
                    print("\n")
        except IndexError as e:
            pass

    def sim(self, row_num, col_num):
        self.count = 0
        print("Now Running Rook Number Simulation\nRows: {}, Cols: {}\n".format(row_num, col_num))
        self.place_in_row(RooksBoard(row_num, col_num), 0)
        print("\nThe Rook Number for a {} x {} board is {}".format(row_num, col_num, self.count))


class SimulationWithNRooks:
    def __init__(self, display=True):
        self.display = display
        self.count = 0

    def place_in_row(self, board, row_idx):
        try:
            row = board.rows[row_idx]
            for col_idx, cell in enumerate(row.row):
                if board.is_valid(row_idx, col_idx):
                    board_copy = board.copy()
                    board_copy.add_rook(row_idx, col_idx)
                    if board_copy.complete_board():
                        self.count += 1
                        if self.display:
                            print("Board number: {}".format(self.count))
                            print(board_copy)
                            print("\n")
                    elif board.num_rows > row_idx + 1:
                        self.place_in_row(board_copy, row_idx + 1)
            if board.num_rows > row_idx + 1:
                self.place_in_row(board, row_idx + 1)
        except IndexError as e:
            pass

    def sim(self, row_num, col_num):
        self.count = 0
        print("Now Running Rook Number Simulation\nRows: {}, Cols: {}\n".format(row_num, col_num))
        self.place_in_row(RooksBoard(row_num, col_num), 0)
        print("\n")
        print("Rook Number: {}".format(self.count))
