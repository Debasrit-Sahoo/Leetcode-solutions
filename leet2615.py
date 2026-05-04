class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ht = defaultdict(list)
        for i, v in enumerate(nums):
            ht[v].append(i)
        
        for pos in ht.values():
            n = len(pos)
            p = 0
            pre = [0]*n

            for i in range(n):
                p += pos[i]
                pre[i] = p

            for j, v in enumerate(pos):
                l = v*j - (pre[j-1] if j > 0 else 0)
                r = (pre[-1] - pre[j]) - v*(n-1-j)
                nums[pos[j]] = l + r

        return nums
        