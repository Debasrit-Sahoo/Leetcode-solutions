class Solution:
    class segtree:
        def __init__(self, k) -> None:
            self.tree = [1] * (k * 2)
            self.k = k
            for par in range(k - 1, 0, -1):
                self.tree[par] = self.tree[par * 2] + self.tree[par * 2 + 1]

        def update(self, id):
            idx = id + self.k
            self.tree[idx] ^= 1
            par_idx = idx >> 1
            cld_idx = idx
            while par_idx:
                self.tree[par_idx] = self.tree[cld_idx] + self.tree[cld_idx ^ 1]
                cld_idx = par_idx
                par_idx >>= 1

        def descend(self, idx):
            while idx < self.k:
                child = idx << 1
                if self.tree[child]: idx = child
                else: idx = child + 1
                
            return idx - self.k

        def query(self, id):
            left = id + self.k
            right = 2*self.k - 1

            rc = -1

            while left <= right:
                if left & 1:
                    if self.tree[left]: return self.descend(left)
                    left += 1
                if not right & 1:
                    if self.tree[right]: rc = right
                    right -= 1

                left >>= 1
                right >>= 1

            if rc != -1:
                return self.descend(rc)

            left = self.k
            right = id + self.k - 1 

            while left <= right:
                if left & 1:
                    if self.tree[left]: return self.descend(left)
                    left += 1
                if not right & 1:
                    if self.tree[right]: rc = right
                    right -= 1

                left >>= 1
                right >>= 1

            if rc != -1:
                return self.descend(rc)
            
            return -1

    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        st = self.segtree(k)
        h = []
        push = heapq.heappush
        pop = heapq.heappop

        cnt = [0] * k

        for i, (time, cost) in enumerate(zip(arrival, load)):
            while h and h[0][0] <= time:
                st.update(pop(h)[1])

            nxt = st.query(i % k)

            if nxt == -1: continue

            push(h, (time + cost, nxt))
            st.update(nxt)
            cnt[nxt] += 1

        mx = max(cnt)
        return [i for i in range(k) if cnt[i] == mx]