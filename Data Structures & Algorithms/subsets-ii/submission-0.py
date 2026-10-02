class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        path = []
        result = []

        def backtrack(start: int) -> None:
            result.append(path[:])

            for i in range(start, len(nums)):
                if i != start and nums[i - 1] == nums[i]:
                    continue

                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result
