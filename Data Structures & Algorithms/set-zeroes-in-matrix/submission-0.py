class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_zero = any(cell == 0 for cell in matrix[0])
        first_col_zero = any(matrix[row][0] == 0 for row in range(len(matrix)))

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if first_row_zero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        
        if first_col_zero:
            for row in range(len(matrix)):
                matrix[row][0] = 0
