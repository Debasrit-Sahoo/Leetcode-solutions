class Solution:
    def evalRPN(self, tokens):
        stack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))
        return stack[0]
    def faster(self, tokens):
        stack = []
        s = set("+-/*") 
        for t in tokens:
            if t not in s:
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    stack.append(a + b)
                if t == "-":
                    stack.append(a - b)
                if t == "*":
                    stack.append(a * b)
                if t == "/":
                    stack.append(int(a / b))
        return stack[0]