class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # fixed size window, check if all slots is 0 at any point
        chars = [0] * 26

        for c in s1:
            chars[ord(c) - ord('a')] += 1

        left = 0
        for right in range(len(s2)):
            chars[ord(s2[right]) - ord('a')] -= 1
            
            # if string is still expanding, continue
            if right - left + 1 != len(s1):
                continue

            # otherwise, check if permutation is satisfied
            if all(freq == 0 for freq in chars):
                return True

            chars[ord(s2[left]) - ord('a')] += 1
            left += 1

        return False

