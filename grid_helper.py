import numpy as np

class Grid:
    def __init__(self, grid: list):
        self.grid_map = np.array(grid)
        self.grid_size = self.grid_map.shape

    def __str__(self):
        return f"Grid(size={self.grid_size})\n{self.grid_map}"

    def is_in_grid(self, position: tuple) -> bool:
        grid_max_row, grid_max_col = self.grid_size
        row, col = position
        return 0 <= row < grid_max_row and 0 <= col < grid_max_col
    
    def get_positions(self, value: str) -> list:
        return list(zip(*np.where(self.grid_map == value)))
    
    def update_value(self, position: tuple, new_value: str):
        row, col = position
        if self.is_in_grid(position):
            self.grid_map[row, col] = new_value

    def get_neighbor_number(self, position: tuple, value: str) -> int:
        row, col = position
        neighbors = [
            (row - 1, col),     # Up
            (row + 1, col),     # Down
            (row, col - 1),     # Left
            (row, col + 1),     # Right
            (row - 1, col - 1), # Up-Left
            (row - 1, col + 1), # Up-Right
            (row + 1, col - 1), # Down-Left
            (row + 1, col + 1)  # Down-Right
        ]
        count = 0
        for n_row, n_col in neighbors:
            if self.is_in_grid((n_row, n_col)) and self.grid_map[n_row, n_col] == value:
                count += 1
        return count