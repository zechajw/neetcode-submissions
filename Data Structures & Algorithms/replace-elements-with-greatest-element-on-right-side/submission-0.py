class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = -1

        for index in range(len(arr) - 1, -1, -1):
            arr[index], max_so_far = max_so_far, max(max_so_far, arr[index])

        return arr