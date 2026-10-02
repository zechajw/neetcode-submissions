class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []

        def backtrack(index: int) -> None:
            result.append(path[:])

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result