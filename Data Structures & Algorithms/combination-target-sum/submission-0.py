class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        result = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return

            if remaining < 0 or start >= len(nums):
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, remaining - nums[i])
                path.pop()

        backtrack(0, target)
        return result
                