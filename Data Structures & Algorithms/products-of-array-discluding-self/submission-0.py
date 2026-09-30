class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Maintain List of Products from the start up to that element
        # Maintain List of Products from end down to that element
        # [1, 2, 2, 3, 4] => [1, 2, 4, 12, 48] listA
        # [1, 2, 2, 3, 4] => [48, 48, 24, 12, 4] listB
        # productExceptSelf(i) for i in range(len(nums)) = listA[i - 1] * listB[i + 1]
        # for left and right bound elements, will be one 

        prefixList = [1] * len(nums)
        suffixList = [1] * len(nums)

        prefixList[0] = nums[0]
        suffixList[-1] = nums[-1]

        # prefix list, product of all numbers before it 
        for i in range(1, len(nums)):
            prefixList[i] = nums[i] * prefixList[i - 1]

        for i in range(2, len(nums) + 1):
            suffixList[-1 * i] = nums[-1 * i] * suffixList[-1 * (i - 1)] 

        resultList = [1] * len(nums)
        for i in range(len(nums)):
            prefixNumber = prefixList[i - 1] if i - 1 >= 0 else 1
            suffixNumber = suffixList[i + 1] if i + 1 < len(nums) else 1
            resultList[i] = prefixNumber * suffixNumber
        
        return resultList
        

