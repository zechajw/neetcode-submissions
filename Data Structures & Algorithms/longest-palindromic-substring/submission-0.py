class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindrome(start: int, end: int) -> tuple[int, int]:
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1

            return (start + 1, end - 1)

        longest_palindrome = ""
        for i in range(len(s)):
            start, end = getPalindrome(i, i)
            if end - start + 1 > len(longest_palindrome):
                longest_palindrome = s[start:end + 1]

            if i + 1 < len(s):
                start, end = getPalindrome(i, i + 1)
                if end - start + 1 > len(longest_palindrome):
                    longest_palindrome = s[start:end + 1]

        return longest_palindrome
            