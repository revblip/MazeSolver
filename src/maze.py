from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window):
        self.cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window

        self.create_cells()

    def create_cells(self):
        for col in range(self.num_cols):
            col_cells = []
            for row in range(self.num_rows):
                col_cells.append(Cell(self.window))
            self.cells.append(col_cells)
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self.draw_cells(col, row)

    def draw_cells(self, col, row):
        if self.window is None:
            return
        x1 = self.x1 + col * self.cell_size_x
        y1 = self.y1 + row * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.cells[col][row].draw(x1, y1, x2, y2)
        self.animate()

    def animate(self):
        if self.window is None:
            return
        self.window.redraw()
        time.sleep(0.05)

