from graphics import Line, Point, Window


def main():
    win = Window(800, 600)
    line = Line(Point(1, 1), Point(100, 100))
    win.draw_line(line, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
