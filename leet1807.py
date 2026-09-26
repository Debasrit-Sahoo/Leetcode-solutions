class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = {}
        for k, v in knowledge:
            d[k] = v

        ans = []
        buffer = []

        a = 0
        for char in s:
            match char:
                case '(':
                    a = True
                case ')':
                    ans.append(d.get("".join(buffer), "?"))
                    buffer = []
                    a = False
                case _:
                    if a:
                        buffer.append(char)
                    else:
                        ans.append(char)

        return "".join(ans)