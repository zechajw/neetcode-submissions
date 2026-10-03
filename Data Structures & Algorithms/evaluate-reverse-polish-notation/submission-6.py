class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isnumeric():
                stack.append(int(token))
                continue
            elif len(token) > 1 and token[0] == '-':
                stack.append(int(token[1:]) * -1)
                continue
            
            # is an operation
            # assume that its always valid
            num2, num1 = stack.pop(), stack.pop()

            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            else:
                stack.append(int(num1 / num2))

        return stack[-1]