import random
import time
from enum import Enum
from typing import Iterator, List, Tuple

from cell import Cell
from graphics import Window


class Direction(Enum):
    RIGHT = (1, 0)
    LEFT = (-1, 0)
    UP = (0, -1)
    DOWN = (0, 1)

    @classmethod
    def __iter__(cls) -> Iterator["Direction"]:
        return iter(cls.__members__.values())

    @property
    def delta(self) -> Tuple[int, int]:
        return self.value


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
        seed=None,
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win: Window | None = win
        self._cells: List[List[Cell]] = []

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

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
        self._cells[top_c][top_r].has_top_wall = False
        self._cells[bot_c][bot_r].has_bottom_wall = False
        self._draw_cell(top_c, top_r)
        self._draw_cell(bot_c, bot_r)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible: List[Direction] = []
            for direction in Direction:
                d_col, d_row = direction.delta
                nxt_col = i + d_col
                nxt_row = j + d_row
                if self._out_of_range(nxt_col, nxt_row):
                    continue
                if not self._cells[nxt_col][nxt_row].visited:
                    possible.append(direction)

            if len(possible) == 0:
                self._draw_cell(i, j)
                return

            random_direction = random.choice(possible)
            nc, nr = self._knock_out_wall(i, j, random_direction)
            self._break_walls_r(nc, nr)

    def _knock_out_wall(self, i: int, j: int, direction: Direction) -> Tuple[int, int]:
        print(i, j, direction)
        dc, dr = direction.delta
        nc, nr = i + dc, j + dr
        match (direction):
            case direction.RIGHT:
                self._cells[i][j].has_right_wall = False
                self._cells[nc][nr].has_left_wall = False
            case direction.LEFT:
                self._cells[i][j].has_left_wall = False
                self._cells[nc][nr].has_right_wall = False
            case direction.UP:
                self._cells[i][j].has_top_wall = False
                self._cells[nc][nr].has_bottom_wall = False
            case direction.DOWN:
                self._cells[i][j].has_bottom_wall = False
                self._cells[nc][nr].has_top_wall = False
        return (nc, nr)

    def _out_of_range(self, col, row):
        return row < 0 or row >= self._num_rows or col < 0 or col >= self._num_cols
