from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def create_line(self, point1_x, point1_y, point2_x, point2_y, color):
        self._win._Window__canvas.create_line(point1_x, point1_y, point2_x, point2_y, fill=color, width=2)
        
    def draw(self):
        if self._win:
            if self.has_left_wall:
                self.create_line(self._x1, self._y1, self._x1, self._y2, "black")
            else:
                self.create_line(self._x1, self._y1, self._x1, self._y2, "white")
            if self.has_right_wall:
                self._win._Window__canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill="black", width=2)
            else:
                self._win._Window__canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill="white", width=2)
            if self.has_top_wall:
                self._win._Window__canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill="black", width=2)
            else:
                self._win._Window__canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill="white", width=2)
            if self.has_bottom_wall:
                self._win._Window__canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill="black", width=2)
            else:
                self._win._Window__canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill="white", width=2)

    


    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)