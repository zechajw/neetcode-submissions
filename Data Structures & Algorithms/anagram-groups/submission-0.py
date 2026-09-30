class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for st in strs:
            key = "".join(sorted(st))

            if key in anagrams:
                anagrams[key].append(st)

            else:
                anagrams[key] = [st]

        return list(anagrams.values())
