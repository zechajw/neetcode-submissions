class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        is_palindrome = [[False for _ in range(len(s))] for _ in range(len(s))]

        # dp[i][j] represents whether dp[i:j] is a palindrome (both inclusive)

        # base cases
        # if j - i < 2 => true
        # dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])

        for length in range(1, len(s) + 1):
            # [0, 1, 2, 3, 4]
            # last element should be len(s) - 1, so the last index of i is len(s) - length
            for i in range(len(s) - length + 1):
                j = i + length - 1
                is_palindrome[i][j] = s[i] == s[j] and (j - i < 2 or is_palindrome[i + 1][j - 1])

        path = []
        result = []
        def backtrack(start: int) -> None:
            if start >= len(s):
                result.append(path[:])
                return

            for end in range(start, len(s)):
                if is_palindrome[start][end]:
                    path.append(s[start:end+1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return result