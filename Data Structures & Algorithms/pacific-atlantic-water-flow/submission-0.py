from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # do bfs from pacific
        pacific_visited = set()

        pacific = deque()

        for col_iter in range(len(heights[0])):
            pacific_visited.add((len(heights) - 1, col_iter))
            pacific.appendleft((len(heights) - 1, col_iter))

        for row_iter in range(len(heights)):
            pacific_visited.add((row_iter, len(heights[0]) - 1))
            pacific.appendleft((row_iter, len(heights[0]) - 1))

        while pacific:
            row, col = pacific.pop()

            neighbours = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

            for n_row, n_col in neighbours:
                if not (0 <= n_row < len(heights) and 0 <= n_col < len(heights[0])):
                    continue

                if (n_row, n_col) in pacific_visited or heights[row][col] > heights[n_row][n_col]:
                    continue

                pacific_visited.add((n_row, n_col))
                pacific.appendleft((n_row, n_col))

        # do bfs from atlantic
        atlantic_visited = set()
        atlantic = deque()

        for col_iter in range(len(heights[0])):
            atlantic_visited.add((0, col_iter))
            atlantic.appendleft((0, col_iter))

        for row_iter in range(len(heights)):
            atlantic_visited.add((row_iter, 0))
            atlantic.appendleft((row_iter, 0))

        while atlantic:
            row, col = atlantic.pop()

            neighbours = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

            for n_row, n_col in neighbours:
                if not (0 <= n_row < len(heights) and 0 <= n_col < len(heights[0])):
                    continue

                if (n_row, n_col) in atlantic_visited or heights[row][col] > heights[n_row][n_col]:
                    continue

                atlantic_visited.add((n_row, n_col))
                atlantic.appendleft((n_row, n_col))


        # get cells that appear in both pacific and atlantic visited set
        result = []

        for row, col in pacific_visited:
            if (row, col) in atlantic_visited:
                result.append([row, col])

        return result
