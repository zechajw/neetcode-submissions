class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1

        while left <= right:
            middle = left + (right - left) // 2

            middle_row = matrix[middle]

            if middle_row[0] <= target <= middle_row[-1]:
                break
            elif target < middle_row[0]:
                right = middle - 1
            else:
                left = middle + 1

        # found the correct row, binary search in the row
        row = matrix[left + (right - left) // 2]

        left, right = 0, len(row) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if row[middle] == target:
                return True
            elif target < row[middle]:
                right = middle - 1
            else:
                left = middle + 1

        return False