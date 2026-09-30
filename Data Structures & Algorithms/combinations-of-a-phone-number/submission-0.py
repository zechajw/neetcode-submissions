class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return mapping[digits]
        
        res = []
        for letter in mapping[digits[0]]:
            res.extend([letter + combination for combination in self.letterCombinations(digits[1:])])

        return res