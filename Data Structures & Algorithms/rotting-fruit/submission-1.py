from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        bfs = deque()
        minutes_taken = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    bfs.appendleft((row, col, 0)) # minutes 0

        while bfs:
            row, col, minutes = bfs.pop()
            minutes_taken = max(minutes_taken, minutes)

            neighbours = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]

            for n_row, n_col in neighbours:
                if not (0 <= n_row < len(grid) and 0 <= n_col < len(grid[0])):
                    continue

                if grid[n_row][n_col] != 1:
                    continue

                grid[n_row][n_col] = 2
                bfs.appendleft((n_row, n_col, minutes + 1))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1

        return minutes_taken