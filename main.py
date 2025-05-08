from cell import Cell
from graphics import Line, Point, Window


def main():
    win = Window(800, 600)
    cell = Cell(50, 50, 100, 100, win)
    cell.draw()
    win.wait_for_close()


if __name__ == "__main__":
    main()
