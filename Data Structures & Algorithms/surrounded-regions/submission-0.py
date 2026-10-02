from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        bfs = deque()

        for col_iter in range(len(board[0])):
            if board[0][col_iter] == 'O':
                bfs.appendleft((0, col_iter))

            if board[len(board) - 1][col_iter] == 'O':
                bfs.appendleft((len(board) - 1, col_iter))

        for row_iter in range(1, len(board) - 1):
            if board[row_iter][0] == 'O':
                bfs.appendleft((row_iter, 0))
            
            if board[row_iter][len(board[0]) - 1] == 'O':
                bfs.appendleft((row_iter, len(board[0]) - 1))

        while bfs:
            row, col = bfs.pop()

            board[row][col] = 'Y'

            neighbours = [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]

            for n_row, n_col in neighbours:
                if not (0 <= n_row < len(board) and 0 <= n_col < len(board[0])):
                    continue

                if board[n_row][n_col] != 'O':
                    continue

                board[n_row][n_col] = 'Y'
                bfs.appendleft((n_row, n_col))

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'Y':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'

                    

        # add all 'O's at the boundaries into the bfs, then mark all 'O's connected to the boundaries with 'Y'
        # at the end, mark all 'Os' as 'X'
        # then mark 'Y' back as 'O'

