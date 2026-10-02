class Solution:
    def countSubstrings(self, s: str) -> int:
        num_palindromes = 0
        def countPalindromes(index1: int, index2: int) -> None:
            nonlocal num_palindromes

            while index1 >= 0 and index2 < len(s) and s[index1] == s[index2]:
                num_palindromes += 1
                index1 -=1
                index2 += 1
            
        for i in range(len(s)):
            countPalindromes(i, i)

            if i + 1 < len(s):
                countPalindromes(i, i + 1)

        return num_palindromes