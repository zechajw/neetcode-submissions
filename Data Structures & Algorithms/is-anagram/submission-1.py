class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_split = [c for c in s]
        t_split = [c for c in t]

        return sorted(s_split) == sorted(t_split)