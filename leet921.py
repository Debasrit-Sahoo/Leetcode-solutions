class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        a = st = 0
        for each in s:
            match each:
                case '(':
                    st += 1
                case _:
                    if st == 0:
                        a += 1
                    else:
                        st -= 1

        return a + abs(st)