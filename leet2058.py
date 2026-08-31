class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> List[int]:
        if not head or not head.next: return [-1, -1]
        prev = head.val
        head = head.next
        cnt = 1

        first = None
        prev_pnt = None
        cur_pnt = None
        mn = 1 << 31
        v = head.val
        while head.next:
            nxt = head.next.val
            if (prev < v > nxt) or (prev > v < nxt):
                if not first:
                    first = cnt
                else:
                    mn = min(cnt - prev_pnt, mn)
                    cur_pnt = cnt
                prev_pnt = cnt

            cnt += 1
            prev = v
            v = nxt
            head = head.next

        if not cur_pnt: return [-1, -1]
        return [mn, cur_pnt - first]