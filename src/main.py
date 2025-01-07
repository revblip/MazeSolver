from graphics import Window
from cell import Cell

def main():
    window = Window(800,600)

    c1 = Cell(window)
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100)
    print(f"Cell 1 coords: {c1.x1}, {c1.y1}, {c1.x2}, {c1.y2}")

    c2 = Cell(window)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(100, 50, 150, 100)
    print(f"Cell 2 coords: {c2.x1}, {c2.y1}, {c2.x2}, {c2.y2}")

    c1.draw_move(c2, True)
    window.wait_for_close()


if __name__ == "__main__":
    main()
