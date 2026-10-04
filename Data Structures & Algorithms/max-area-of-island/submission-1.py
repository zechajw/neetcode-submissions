from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(max_area, self.getIslandArea(grid, row, col))

        return max_area        

    def getIslandArea(self, grid: List[List[int]], row: int, col: int) -> int:
        """
        Gets area of island, then marks all cells in island as 0 to avoid recounting
        """
        bfs = deque()

        bfs.appendleft((row, col))
        area = 0
        grid[row][col] = 0

        while bfs:
            row, col = bfs.pop()
            area += 1
            for n_row, n_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]) and grid[n_row][n_col] == 1:
                    bfs.appendleft((n_row, n_col))
                    grid[n_row][n_col] = 0

        return area