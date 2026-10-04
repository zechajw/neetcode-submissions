class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 in num_set:
                continue

            length = 0
            curr_num = num

            # lets say we have [1, 2, 3, 4]
            # curr_num = 1, length = 1
            # curr_num = 2, length = 2
            # curr_num = 3, length = 3
            # curr_num = 4, length = 4
            # curr_num = 5 break

            while curr_num in num_set:
                curr_num += 1
                length +=1

            max_length = max(max_length, length)

        return max_length

