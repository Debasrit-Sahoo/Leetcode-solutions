class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = [[set(), set(), False]]

        for char in expression:
            match char:
                case "{":
                    stack.append([set(), set(), False])
                case "}":
                    c = stack.pop()
                    operand = c[0] | c[1]

                    if stack[-1][2]:
                        stack[-1][0] = {a + b for a in stack[-1][0] for b in operand}
                    else:
                        stack[-1][0] |= operand

                    stack[-1][2] = True

                case ",":
                    stack[-1][1] |= stack[-1][0]
                    stack[-1][0].clear()
                    stack[-1][2] = False
                case _:
                    if stack[-1][2]:
                        stack[-1][0] = {x + char for x in stack[-1][0]}
                    else:
                        stack[-1][0].add(char)

                    stack[-1][2] = True

        return sorted(stack[0][0] | stack[0][1])