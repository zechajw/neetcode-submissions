from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi-source bfs
        INF_VALUE = 2147483647

        bfs = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    bfs.appendleft((row, col, 0)) # starting distance from each source is 0

        while bfs:
            row, col, distance = bfs.pop()

            neighbours = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

            for n_row, n_col in neighbours:
                if not (0 <= n_row < len(grid) and 0 <= n_col < len(grid[0])):
                    continue

                if grid[n_row][n_col] != INF_VALUE:
                    continue

                grid[n_row][n_col] = distance + 1
                bfs.appendleft((n_row, n_col, distance + 1))


        
