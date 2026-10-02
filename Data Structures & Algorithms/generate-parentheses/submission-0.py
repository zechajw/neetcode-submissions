class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # max length of path = n * 2
        path = []
        result = []

        def backtrack(used: int, depth: int) -> None:
            nonlocal n
            if len(path) > n * 2:
                return

            if depth == 0 and used == n:
                result.append("".join(path))
                return

            if used < n:
                path.append("(")
                backtrack(used + 1, depth + 1)
                path.pop()

            if depth > 0:
                path.append(")")
                backtrack(used, depth - 1)
                path.pop()

        backtrack(0, 0)
        return result