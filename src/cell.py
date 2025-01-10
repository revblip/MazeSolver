from graphics import Point, Line

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.window = window

    def draw(self, x1, y1, x2, y2):
        print(f"Setting coordinates: x1={x1}, y1={y1}, x2={x2}, y2={y2}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        print(f"After setting: self.x1={self.x1}, self.y1={self.y1}, self.x2={self.x2}, self.y2={self.y2}")
        if self.window is None:
            return
        if self.has_left_wall:
            line = Line(Point(x1,y1),Point(x1,y2))
            self.window.draw_line(line)
        else:
            line = Line(Point(x1,y1),Point(x1,y2))
            self.window.draw_line(line, "red")
        if self.has_right_wall:
            line = Line(Point(x2,y1),Point(x2,y2))
            self.window.draw_line(line)
        else:
            line = Line(Point(x2,y1),Point(x2,y2))
            self.window.draw_line(line, "red")
        if self.has_top_wall:
            line = Line(Point(x1,y1),Point(x2,y1))
            self.window.draw_line(line)
        else:
            line = Line(Point(x1,y1),Point(x2,y1))
            self.window.draw_line(line, "red")
        if self.has_bottom_wall:
            line = Line(Point(x1,y2),Point(x2,y2))
            self.window.draw_line(line)
        else:
            line = Line(Point(x1,y2),Point(x2,y2))
            self.window.draw_line(line, "red")

    def draw_move(self, other, undo=False):
        self_center_x = (self.x1 + self.x2) // 2 # ignore this error
        self_center_y = (self.y1 + self.y2) // 2 # ignore this error
        other_center_x = (other.x1 + other.x2) // 2
        other_center_y = (other.y1 + other.y2) // 2

        line = Line(Point(self_center_x, self_center_y), Point(other_center_x, other_center_y))
        if undo:
            self.window.draw_line(line, "gray")
        else:
            self.window.draw_line(line, "red")


