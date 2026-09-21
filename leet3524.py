class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        prev = [0] * k 
        nxt = [0] * k
        ans = [0] * k

        x = nums[0] % k
        prev[x] = ans[x] = 1

        for x in nums[1:]:
            x %= k
            for r in range(k):
                nxt[(r * x) % k] += prev[r]
            
            nxt[x] += 1

            prev, nxt = nxt, prev
            for i in range(k):
                ans[i] += prev[i]
                nxt[i] = 0
            
        return ans