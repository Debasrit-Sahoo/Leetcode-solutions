class Solution:
    def checkValidString(self, s: str) -> bool:
        cnt = st = 0
        for ch in s:
            if ch == '*':
                cnt += 1
            elif ch == '(':
                st += 1
            else:
                st -= 1

                if st < 0:
                    if cnt == 0:
                        return False
                    cnt -= 1
                    st = 0

        if st > cnt: return False

        st = cnt = 0
        for ch in reversed(s):
            if ch == '*':
                cnt += 1
            elif ch == ')':
                st += 1
            else:
                st -= 1

                if st < 0:
                    if cnt == 0:
                        return False
                    cnt -= 1
                    st = 0

        return st <= cnt