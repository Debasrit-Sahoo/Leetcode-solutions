class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        hp = heapq.heappush
        x = Counter(nums)
        for n, f in x.items():
            hp(pq, (-f, n))

        hpp = heapq.heappop

        out = []
        for _ in range(k):
            out.append(hpp(pq)[1])

        return out