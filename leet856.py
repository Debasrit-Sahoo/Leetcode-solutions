class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for char in s:
            if char == ')':
                if stack[-1] == '(':
                    stack[-1] = 1
                else:
                    t = 0
                    while stack[-1] != '(':
                        t += stack.pop()
                    stack[-1] = t << 1

            else:
                stack.append('(')

        return sum(stack)