class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        step = [1] * n

        # 3rd step,
        # 1 ste 

        step[0] = 1 # 1 way to get to 1st step
        step[1] = 2 # 2 ways to get to 2nd step

        for i in range(2, n):
            step[i] = step[i - 1] + step[i - 2]

        return step[-1]
            
