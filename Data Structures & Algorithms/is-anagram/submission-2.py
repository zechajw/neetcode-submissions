class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_split = [c for c in s]
        t_split = [c for c in t]

        s_split.sort()
        t_split.sort()

        return all([s_split[i] == t_split[i] for i in range(len(s_split))])

        