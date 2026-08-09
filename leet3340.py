class Solution:
    def pack(self, rem: List[int]):
        cnt = [0] * 10

        cnt[2] = rem[0]
        cnt[3] = rem[1]
        cnt[5] = rem[2]
        cnt[7] = rem[3]

        cnt[8] = cnt[2] // 3
        cnt[2] %= 3

        cnt[9] = cnt[3] // 2
        cnt[3] %= 2

        cnt[4] = cnt[2] // 2
        cnt[2] %= 2

        cnt[6] = min(cnt[2], cnt[3])
        cnt[2] -= cnt[6]
        cnt[3] -= cnt[6]

        if cnt[3] and cnt[4]:
            cnt[3] -= 1
            cnt[4] -= 1
            cnt[2] += 1
            cnt[6] += 1

        return cnt
    def smallestNumber(self, num: str, t: int) -> str:
        need = [0] * 4

        for j, p in enumerate((2, 3, 5, 7)):
            while t % p == 0:
                t //= p
                need[j] += 1

        if t != 1: return "-1"

        factor = {
            '0': (0, 0, 0, 0),
            '1': (0, 0, 0, 0),
            '2': (1, 0, 0, 0),
            '3': (0, 1, 0, 0),
            '4': (2, 0, 0, 0),
            '5': (0, 0, 1, 0),
            '6': (1, 1, 0, 0),
            '7': (0, 0, 0, 1),
            '8': (3, 0, 0, 0),
            '9': (0, 2, 0, 0)
        }

        n = len(num)
        pref = [0] * 4
        for c in num:
            f = factor[c]
            for j in range(4):
                pref[j] += f[j]

        z = num.find('0')

        if z == -1 and all(pref[j] >= need[j] for j in range(4)):
            return num

        for i in range(n - 1, -1, -1):

            f = factor[num[i]]
            for j in range(4):
                pref[j] -= f[j]

            if z != -1 and i > z: continue

            for d in range(int(num[i]) + 1, 10):

                f = factor[str(d)]

                rem = [max(0, need[j] - pref[j] - f[j]) for j in range(4)]

                slen = n - i - 1
                suf = self.pack(rem)

                if sum(suf) > slen:
                    continue

                res = ['1'] * (slen - sum(suf))

                for x in range(2, 10):
                    res.extend([str(x)] * suf[x])

                return num[:i] + str(d) + ''.join(res)

        suf = self.pack(need)
        length = max(n + 1, sum(suf))

        res = ['1'] * (length - sum(suf))

        for x in range(2, 10):
            res.extend([str(x)] * suf[x])

        return ''.join(res)