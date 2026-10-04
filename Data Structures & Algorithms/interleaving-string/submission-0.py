class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = {}
        def dp(index_1: int, index_2: int) -> bool:
            
            if (index_1, index_2) in memo:
                return memo[(index_1, index_2)] 

            # if index_1 is at 0 and index_2 is at 1, index_3 is at 1
            index_3 = index_1 + index_2

            if index_1 >= len(s1):
                can_interleave = s2[index_2:] == s3[index_3:]
                memo[(index_1, index_2)] = can_interleave
            elif index_2 >= len(s2):
                can_interleave = s1[index_1:] == s3[index_3:]
                memo[(index_1, index_2)] = can_interleave
            else:
                if s1[index_1] == s3[index_3] and dp(index_1 + 1, index_2):
                    memo[(index_1, index_2)] = True

                elif s2[index_2] == s3[index_3] and dp(index_1, index_2 + 1):
                    memo[(index_1, index_2)] = True
                else:
                    memo[(index_1, index_2)] = False

            return memo[(index_1, index_2)]

        return dp(0, 0)

            