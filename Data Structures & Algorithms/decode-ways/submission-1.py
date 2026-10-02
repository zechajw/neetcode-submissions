class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def backtrack(index: int) -> int:
            if index == len(s):
                return 1

            if s[index] == '0':
                return 0

            if index in memo:
                return memo[index]

            num_ways = 0
            num_ways += backtrack(index + 1)

            # check if valid two digit form can be made
            if index + 1 < len(s) and int(s[index:index+2]) <= 26:
                num_ways += backtrack(index + 2)

            memo[index] = num_ways
            return num_ways

        return backtrack(0)

            
