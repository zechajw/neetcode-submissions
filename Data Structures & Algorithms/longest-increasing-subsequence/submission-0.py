from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # we keep an array of tails, where tails[i] represents a chain of length i + 1 that ends at tails[i]
        # for each number, we binary search the tails array for the insertion point

        # if the current element is bigger than the last element in the tails array, we append it and create a longer tail from there
        # otherwise, we search for the smallest point to insert it
        tails = []
    
        for num in nums:
            insert_index = bisect_left(tails, num)

            if insert_index < len(tails):
                tails[insert_index] = num
            else:
                tails.append(num)

        return len(tails)