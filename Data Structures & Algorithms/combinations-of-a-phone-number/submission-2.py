class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        path = []
        result = []
        
        letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrack(index: int) -> None:
            if index >= len(digits):
                result.append("".join(path))
                return

            for letter in letters[digits[index]]:
                path.append(letter)
                backtrack(index + 1)
                path.pop()

        backtrack(0)
        return result
