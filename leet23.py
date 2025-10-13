def mergeKLists(arr):
        dummy = ListNode(0)
        cur = dummy
        while arr:
            lowest = arr[0]
            index_in_arr = 0
            for i,v in enumerate(arr):
                if v.val < lowest.val:
                    lowest = v
                    index_in_arr = i
            cur.next = lowest
            cur = cur.next
            c = arr[index_in_arr].next
            arr[index_in_arr] = arr[index_in_arr].next
            if arr[index_in_arr] is None:
                arr.pop(index_in_arr)
        return dummy.next