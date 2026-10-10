class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        heap = [[-num, cnt] for num, cnt in Counter(diff).items()]
        heapq.heapify(heap)
        k = k1 + k2
        pop = heapq.heappop
        push = heapq.heappush
        ans = 0

        while k and heap and heap[0][0] != 0:
            x = pop(heap)
            num, cnt = -x[0], x[1]
            if k >= cnt:

                if heap and -heap[0][0] == num-1:
                    heap[0][1] += cnt

                else:
                    x[0] = -(num - 1)
                    push(heap, x)

                k -= cnt

            else:                
                ans += num ** 2 * (cnt - k)
                ans += (num - 1) ** 2 * (k)
                break

        return ans + sum(num ** 2 * cnt for num, cnt in heap)