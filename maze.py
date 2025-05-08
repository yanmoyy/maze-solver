import time
from typing import List

from cell import Cell
from graphics import Window


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win: Window | None = win
        self._cells: List[List[Cell]] = []

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self) -> None:
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int):
        x1 = self._x1 + self._cell_size_x * i
        y1 = self._y1 + self._cell_size_y * j
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is not None:
            self._win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        top_c, top_r = 0, 0
        bot_c, bot_r = self._num_cols - 1, self._num_rows - 1
        top_left_cell = self._cells[top_c][top_r]
        bottom_right_cell = self._cells[bot_c][bot_r]
        top_left_cell.has_top_wall = False
        self._draw_cell(top_c, top_r)
        self._draw_cell(bot_c, bot_r)
        bottom_right_cell.has_bottom_wall = False
