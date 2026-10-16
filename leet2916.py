class Solution:
    class segtree:
        def __init__(self, n) -> None:
            self.MOD = 10**9 + 7
            n <<= 2
            self.sq = [0] * n
            self.sm = [0] * n
            self.lz = [0] * n

        def pd(self, node, lo, hi):
            if not self.lz[node]: return

            mid = (lo + hi) // 2
            x = 2 * node
            v = self.lz[node]
            ln = mid - lo + 1
            self.sq[x] = (self.sq[x] + self.sm[x] * 2 * v + v * v * ln) % self.MOD
            self.sm[x] = (self.sm[x] + v * ln) % self.MOD
            self.lz[x] = (self.lz[x] + v) % self.MOD
            x += 1
            ln = hi - mid
            self.sq[x] = (self.sq[x] + self.sm[x] * 2 * v + v * v * ln) % self.MOD
            self.sm[x] = (self.sm[x] + v * ln) % self.MOD
            self.lz[x] = (self.lz[x] + v) % self.MOD
            self.lz[node] = 0

        def update(self, node, lo, hi, l, r):
            if hi < l or lo > r: return
            if l <= lo and hi <= r:
                ln = hi - lo + 1
                self.sq[node] = (self.sq[node] + self.sm[node] * 2 + ln) % self.MOD
                self.sm[node] = (self.sm[node] + ln) % self.MOD
                self.lz[node] = (self.lz[node] + 1) % self.MOD
            else:
                self.pd(node, lo, hi)
                mid = (lo + hi) // 2
                self.update(node*2, lo, mid, l, r)
                self.update(node*2 + 1, mid + 1, hi, l, r)
                self.sq[node] = (self.sq[node*2] + self.sq[node*2+1]) % self.MOD
                self.sm[node] = (self.sm[node*2] + self.sm[node*2+1]) % self.MOD

    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        n = len(nums)
        ans = 0
        last = {}
        seg = self.segtree(n)

        for j in range(n):
            p = last.get(nums[j], -1)
            seg.update(1, 0, n-1, p+1, j)
            ans = (ans + seg.sq[1]) % MOD
            last[nums[j]] = j

        return ans