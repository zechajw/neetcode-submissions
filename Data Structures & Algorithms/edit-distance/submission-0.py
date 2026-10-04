class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = {}

        def dp(index_1: int, index_2: int) -> int:
            if index_1 == len(word1) and index_2 == len(word2):
                return 0
            elif index_1 == len(word1):
                # have to insert the rest of the characters
                return len(word2) - index_2
            elif index_2 == len(word2):
                return len(word1) - index_1

            if (index_1, index_2) in memo:
                return memo[(index_1, index_2)]

            if word1[index_1] == word2[index_2]:
                min_ways = dp(index_1 + 1, index_2 + 1)
                memo[(index_1, index_2)] = min_ways
            else:
                del_char = dp(index_1 + 1, index_2)
                insert_char = dp(index_1, index_2 + 1)
                replace_char = dp(index_1 + 1, index_2 + 1)
                min_ways = min(del_char, insert_char, replace_char) + 1
                memo[(index_1, index_2)] = min_ways

            return memo[(index_1, index_2)]
        
        return dp(0, 0)