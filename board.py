import copy


class Row:
    def __init__(self, cols):
        self.row = [False for col in range(0, cols)]

    def set_cell(self, col, value):
        self.row[col] = value

    def __str__(self):
        return "|{}|".format("|".join(["x" if cell else " " for cell in self.row]))


class Board:
    def __init__(self, rows, cols):
        self.rows = [Row(cols) for row in range(0, rows)]
        self.num_cols = cols
        self.num_rows = rows

    def set_cell(self, row, col, value):
        self.rows[row].set_cell(col, value)

    def get_cell(self, row, col):
        return self.rows[row][col]

    def copy(self):
        return copy.deepcopy(self)

    def __str__(self):
        return "\n".join([str(row) for row in self.rows])


class RooksBoard(Board):
    def __init__(self, rows, cols):
        Board.__init__(self, rows, cols)
        self.num_rooks = 0

    def is_valid(self, row, col):
        return self._check_row(row) and self._check_col(col)

    def add_rook(self, row, col):
        self.set_cell(row, col, True)
        self.num_rooks += 1

    def del_rook(self, row, col):
        self.set_cell(row, col, False)
        self.num_rooks -= 1

    def complete_board(self):
        return self.num_rooks >= min(self.num_cols, self.num_rows)

    def _check_row(self, row):
        return True not in self.rows[row].row

    def _check_col(self, col):
        col = [row.row[col] for row in self.rows]
        return True not in col


if __name__ == "__main__":
    r = Row(2)
    print(r)
    print("+++++++++++++++++++++++")
    r.set_cell(1, True)
    print(r)
    print("+++++++++++++++++++++++")
    b = Board(3, 3)
    b1 = RooksBoard(5, 7)
    print(b)
    print("+++++++++++++++++++++++")
    print(b1)
    b1.set_cell(1, 2, True)
    print("+++++++++++++++++++++++")
    print(b1)

    print(b1._check_row(1))
    print(b1._check_row(2))
    print(b1._check_col(2))
