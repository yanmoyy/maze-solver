from cell import Cell
from graphics import Line, Point, Window


def main():
    win = Window(800, 600)
    cell1 = Cell(50, 50, 100, 100, win)
    cell2 = Cell(200, 200, 250, 250, win)
    cell1.draw()
    cell2.draw()
    cell1.draw_move(cell2)
    win.wait_for_close()


if __name__ == "__main__":
    main()
