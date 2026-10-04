class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curr_row = [1] * n

        for _ in range(1, m):
            next_row = [0] * n
            next_row[0] = 1

            for col in range(1, n):
                next_row[col] = curr_row[col] + next_row[col - 1]
            
            curr_row = next_row

        return curr_row[-1]