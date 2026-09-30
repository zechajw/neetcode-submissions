class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestConsecutiveLength = 1 if len(nums) > 0 else 0
        numSet = set(nums)
        
        for num in numSet:
            if num - 1 in numSet:
                continue
            
            consecutiveLength = 1
            currNum = num + 1

            while currNum in numSet:
                consecutiveLength += 1
                currNum += 1

            longestConsecutiveLength = max(consecutiveLength, longestConsecutiveLength)
        
        return longestConsecutiveLength

            