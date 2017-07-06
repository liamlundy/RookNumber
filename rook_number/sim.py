from rook_number.board import RooksBoard


class Simulation:
    def __init__(self, display=False, find_k_rooks=True):
        self.find_k_rooks = find_k_rooks
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
                self.place_in_row(board, row_idx + 1)  # Maybe make copy first
            elif self.find_k_rooks or board.complete_board():
                self.count += 1
                if self.display:
                    print("Board number: {}".format(self.count))
                    print(board)
                    print("\n")
        except IndexError as e:
            print(e)

    def run(self, row_num, col_num):
        self.count = 0
        sim_type = 'K' if self.find_k_rooks else 'N'
        print(
            "Now Running Rook Number Simulation for {} Rooks\nRows: {}, Cols: {}\n".format(sim_type, row_num, col_num)
        )
        self.place_in_row(RooksBoard(row_num, col_num), 0)
        print("The Rook Number for a {} x {} board is {}".format(row_num, col_num, self.count))


sim = Simulation()
sim.run(3, 3)
