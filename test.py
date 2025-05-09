import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def create_maze(self, num_cols=12, num_rows=10):
        return Maze(0, 0, num_rows, num_cols, 10, 10)

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = self.create_maze(num_cols, num_rows)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_enterance_and_exit(self):
        m1 = self.create_maze()
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(
            m1._cells[m1._num_cols - 1][m1._num_rows - 1].has_bottom_wall, False
        )

    def test_reset_cells_visited(self):
        m1 = self.create_maze()
        for col in m1._cells:
            for cell in col:
                self.assertEqual(False, cell.visited)


if __name__ == "__main__":
    unittest.main()
