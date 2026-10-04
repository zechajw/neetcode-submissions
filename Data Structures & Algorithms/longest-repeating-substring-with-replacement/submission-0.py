class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = [0] * 26

        max_length = 0

        left = 0
        for right in range(len(s)):
            chars[ord(s[right]) - ord('A')] += 1

            while sum(chars) - max(chars) > k:
                chars[ord(s[left]) - ord('A')] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length