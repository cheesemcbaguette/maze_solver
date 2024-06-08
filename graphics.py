from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # Initialize root Tk widget
        self.__root = Tk()
        self.__root.title("Tkinter Window")
        self.__root.geometry(f"{width}x{height}")
        
        # Create and pack canvas
        self.__canvas = Canvas(self.__root, bg="white")
        self.__canvas.pack(fill=BOTH, expand=True)
        
        # Initialize running state
        self.__running = False
        
        # Handle window close event
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        # Redraw the window
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        # Set running state to True and keep redrawing the window until closed
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        # Set running state to False to stop the window loop
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill=fill_color, width=2
        )
