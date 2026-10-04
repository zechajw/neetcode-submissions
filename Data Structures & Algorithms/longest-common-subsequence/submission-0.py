class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(index_1: int, index_2: int) -> int:
            if index_1 >= len(text1):
                return 0
            
            if index_2 >= len(text2):
                return 0

            if (index_1, index_2) in memo:
                return memo[(index_1, index_2)]

            if text1[index_1] == text2[index_2]:
                longest_subsequence =  1 + dfs(index_1 + 1, index_2 + 1)
            else:
                longest_subsequence = max(dfs(index_1 + 1, index_2), dfs(index_1, index_2 + 1))

            memo[(index_1, index_2)] = longest_subsequence
            return memo[(index_1, index_2)]

        return dfs(0, 0)