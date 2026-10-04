class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right, up, down = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        spiral_order = []
        while up <= down and left <= right:
            # go left
            for col in range(left, right + 1):
                spiral_order.append(matrix[up][col])
            up += 1

            # go down
            for row in range(up, down + 1):
                spiral_order.append(matrix[row][right])

            right -= 1

            # go right
            if up <= down:
                for col in range(right, left - 1, -1):
                    spiral_order.append(matrix[down][col])

                down -= 1

            # go up
            if left <= right:
                for row in range(down, up - 1, -1):
                    spiral_order.append(matrix[row][left])
                left += 1

        return spiral_order
        