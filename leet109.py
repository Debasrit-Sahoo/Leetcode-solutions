def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        def n(lo, hi):
            if lo >= hi:
                return None
            mid = (lo + hi) >> 1
            root = TreeNode(nums[mid],n(lo, mid),n(mid + 1, hi))
            return root
        return n(0, len(nums))