class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]

        for each in s:
            match each:
                case '(':
                    stack.append([])
                case ')':
                    e = "".join(stack.pop())[::-1]
                    stack[-1].append(e)
                case _:
                    stack[-1].append(each)

        return "".join(stack.pop())