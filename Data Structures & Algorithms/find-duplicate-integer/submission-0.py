class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

        # [1, 2, 3, 4, 4]
        # slow = 1, fast = 1
        # slow = 2, fast = 3
        # slow = 3, fast = 4
        # slow = 4, fast = 4
