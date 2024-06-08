from graphics import Line, Point, Window
from cell import Cell
from maze import Maze

# Main function to create and display the window
if __name__ == "__main__":
    win = Window(800, 600)
    maze = Maze(50, 50, 10, 10, 40, 40, win)
    win.wait_for_close()