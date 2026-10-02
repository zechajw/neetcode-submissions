class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()

        def dfs(index: int, row: int, col: int) -> bool:
            if index == len(word) - 1:
                return board[row][col] == word[index]

            neighbours = [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]

            valid_neighbours = [(r, c) for r, c in neighbours if 0 <= r < len(board) and 0 <= c < len(board[0]) and (r, c) not in visited and board[r][c] == word[index + 1]]

            for n_row, n_col in valid_neighbours:
                visited.add((n_row, n_col))
                if dfs(index + 1, n_row, n_col):
                    return True
                visited.remove((n_row, n_col))

            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    visited.add((row, col))
                    if dfs(0, row, col):
                        return True
                    visited.remove((row, col))

        return False
