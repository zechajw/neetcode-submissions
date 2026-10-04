from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    num_islands += 1
                    self.countIsland(grid, row, col)

        return num_islands

    def countIsland(self, grid: List[List[str]], row: int, col: int) -> None:
        # mark the whole island as visited giving a starting cell
        bfs = deque()
        bfs.appendleft((row, col))

        while bfs:
            row, col = bfs.pop()
            for n_row, n_col in [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]:
                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]) and grid[n_row][n_col] == '1':
                    bfs.appendleft((n_row, n_col))
                    grid[n_row][n_col] = '0'

        return 