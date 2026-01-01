from typing import List
class Solution:
    def tokenizer(self, s: str) -> List:
        l = []
        out = []
        for ch in s:
            if ch.isdigit():
                l.append(ch)
            elif ch == " ":
                continue
            else:
                if l:
                    if len(l) == 1 and l[0] == "-" and ch == "(":
                        l.clear()
                        out.append(-1)
                        out.append("*")
                        out.append(ch)
                        continue
                    out.append(int("".join(l)))
                    l.clear()
                if ch == "-" and (not out or (isinstance(out[-1], str) and out[-1] != ")")):
                    l.append("-")
                    continue
                out.append(ch)
        if l:
            out.append(int("".join(l)))
        return out
    class node:
        def __init__(self, val, l , r) -> None:
            self.val = val
            self.left = l
            self.right = r
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        def evaluate(self) -> int:
            if isinstance(self.val, int): return self.val
            l, r = self.left.evaluate(), self.right.evaluate()
            return self.ops[self.val](l, r)       
    def brac_pre_parse(self, l: List) -> node:
        stack = []
        for ch in l:
            if ch == ")":
                t = []
                while stack and stack[-1] != "(":
                    t.append(stack.pop())
                stack.pop()
                stack.append(self.parser(t))
            else:
                stack.append(ch)
        stack.reverse()
        return self.parser(stack)
    def parser(self, l: List) -> node:
        if len(l) == 1:
            return l[0] if isinstance(l[0], self.node) else self.node(l[0], None, None)
        op1 = op2 = -1
        for i, n in enumerate(l):
            if not isinstance(n, str): continue
            if op1 == -1 and n in ["+", "-"]:
                op1 = i
                break
            elif op2 == -1 and n in ["*", "/"]:
                op2 = i
        x = op1 if op1 >= 0 else op2

        return self.node(l[x], self.parser(l[1+x:]), self.parser(l[:x]))
    def calculate(self, s: str) -> int:
        return self.brac_pre_parse(self.tokenizer(s)).evaluate()