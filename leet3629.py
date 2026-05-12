class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        mx = max(nums)
        
        numz = defaultdict(list)
        for i, v in enumerate(nums):
            numz[v].append(i)

        tele = defaultdict(list)

        is_prime = [True] * (mx + 1)
        is_prime[0] = is_prime[1] = False

        for p in range(2, mx + 1):
            if not is_prime[p]: continue

            for fac in range(p, mx + 1, p):
                is_prime[fac] = False
                if fac in numz:
                    tele[p].extend(numz[fac])
            is_prime[p] = True

        q = deque([0])
        vis = [False]*n
        vis[0] = True

        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()
                if i == n-1: return steps

                a, b= i-1, i+1
                if a >= 0 and not vis[a]:
                    vis[a] = True
                    q.append(a)
                if b < n and not vis[b]:
                    vis[b] = True
                    q.append(b)

                val = nums[i]

                for j in tele.pop(val, []):

                    if not vis[j]:
                        vis[j] = True
                        q.append(j)
            steps+=1
        return -1