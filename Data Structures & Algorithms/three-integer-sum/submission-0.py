class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = []

        for index, num in enumerate(nums):
            if index > 0 and nums[index - 1] == nums[index]:
                continue

            left, right = index + 1, len(nums) - 1

            while left < right:
                if left > index + 1 and nums[left - 1] == nums[left]:
                    left += 1
                    continue
                elif right < len(nums) - 1 and nums[right + 1] == nums[right]:
                    right -= 1
                    continue

                triplet_sum = nums[left] + nums[right] + num

                if triplet_sum == 0:
                    triplets.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif triplet_sum > 0:
                    right -= 1
                else:
                    left += 1

        return triplets
