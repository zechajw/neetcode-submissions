class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        used_indexes = set()
        result = []

        def backtrack() -> None:
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if i not in used_indexes:
                    path.append(nums[i])
                    used_indexes.add(i)
                    backtrack()
                    path.pop()
                    used_indexes.remove(i)

        backtrack()
        return result
                     