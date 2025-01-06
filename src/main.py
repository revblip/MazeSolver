from graphics import Window, Point, Line

def main():
    window = Window(800,600)
    line_one = Line(Point(50,50), Point(100,100))
    window.draw_line(line_one)
    window.wait_for_close()


if __name__ == "__main__":
    main()

