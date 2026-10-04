class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            tuple_key = self.getAnagramCount(string)

            anagrams[tuple_key].append(string)

        return [value for value in anagrams.values()]

    def getAnagramCount(self, string: str):
        # returns tuple of 26 positive integer counts, each representing the count of each character
        counter = [0] * 26

        for c in string:
            counter[ord(c) - ord('a')] += 1

        return tuple(counter)