from graphics import Line, Point, Window


class Cell:
    def __init__(self, win) -> None:
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win: Window | None = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1: float, y1: float, x2: float, y2: float):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def get_center(self) -> Point:
        if self._x1 is None or self._x2 is None or self._y1 is None or self._y2 is None:
            raise Exception("Need draw first")
        center_x = (self._x1 + self._x2) / 2
        center_y = (self._y1 + self._y2) / 2
        return Point(center_x, center_y)

    def draw_move(self, to_cell: "Cell", undo=False):
        if self._win is None:
            return
        center_1 = self.get_center()
        center_2 = to_cell.get_center()
        line = Line(center_1, center_2)
        fill_color = "red"
        if undo:
            fill_color = "gray"
        self._win.draw_line(line, fill_color)
