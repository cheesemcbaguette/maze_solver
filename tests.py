import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )
    
    def test_break_walls_r(self):
        num_cols = 12
        num_rows = 10
        seed = 42
        m = Maze(0, 0, num_rows, num_cols, 10, 10, seed=seed)
        
        all_visited = all(cell.visited for row in m._cells for cell in row)
        self.assertTrue(all_visited)

        # Ensure that at least some walls have been broken
        walls_intact = all(cell.has_left_wall and cell.has_right_wall and cell.has_top_wall and cell.has_bottom_wall for row in m._cells for cell in row)
        self.assertFalse(walls_intact)

        
if __name__ == "__main__":
    unittest.main()