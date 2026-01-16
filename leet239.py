class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        out = []

        for i, n in enumerate(nums):
            while q and nums[q[-1]] < n:
                q.pop()
            q.append(i)
            if q[0] <= (i - k): q.popleft()
            if i >= k - 1: out.append(nums[q[0]])
        return out