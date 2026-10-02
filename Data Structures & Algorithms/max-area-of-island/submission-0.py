from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(row: int, col: int) -> int:
            # conduct bfs from this island and return the size of the island at the end
            island_size = 1

            bfs = deque()

            bfs.appendleft((row, col))
            grid[row][col] = 0
            while bfs:
                row, col = bfs.pop()

                neighbours = [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]
                valid_neighbours = [(n_row, n_col) for n_row, n_col in neighbours if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]) and grid[n_row][n_col] == 1]

                for n_row, n_col in valid_neighbours:
                    grid[n_row][n_col] = 0
                    island_size += 1
                    bfs.appendleft((n_row, n_col))

            return island_size

        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(max_area, bfs(row, col))

        return max_area

