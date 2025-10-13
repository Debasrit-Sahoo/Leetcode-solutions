from heapq import heappop, heappush
def mergeKLists(arr):
        heap = []
        dummy = ListNode(0)
        cur = dummy
        for i, v in enumerate(arr):
            if v:
                heappush(heap, (v.val, i , v))
        while heap:
            val, i, v = heappop(heap)
            cur.next = v
            cur = cur.next

            if v.next:
                heappush(heap, (v.next.val, i, v.next))
        return dummy.next