class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(s_index: int, t_index: int) -> int:
            if t_index >= len(t):
                return 1

            if s_index >= len(s):
                return 0

            if (s_index, t_index) in memo:
                return memo[(s_index, t_index)]

            num_ways = 0
            if s[s_index] == t[t_index]:
                num_ways += dfs(s_index + 1, t_index + 1)
            
            num_ways += dfs(s_index + 1, t_index)
            memo[(s_index, t_index)] = num_ways
            return num_ways

        return dfs(0, 0)
        