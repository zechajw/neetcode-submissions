class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # we conduct a dfs from each cell, and its result is the longest strictly increasing path from that cell
        # if we encounter a cell from before, we add it directly
        max_length = 1

        longest_path = [[-math.inf for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                max_length = max(max_length, self.dfs(matrix, longest_path, row, col))

        return max_length
    

    def dfs(self, matrix: List[List[int]], longest_path: List[List[int]], row: int, col: int) -> int:
        if longest_path[row][col] != -math.inf:
            return longest_path[row][col]

        path = 1

        for n_row, n_col in [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]:
            if 0 <= n_row < len(matrix) and 0 <= n_col < len(matrix[0]) and matrix[n_row][n_col] > matrix[row][col]:
                path = max(path, 1 + self.dfs(matrix, longest_path, n_row, n_col))

        longest_path[row][col] = path
        return path