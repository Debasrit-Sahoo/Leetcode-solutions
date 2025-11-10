def sortedArrayToBST(nums):
        def build(lo,hi):
            print(lo, hi)
            if lo>=hi:
                return None
            mid = ( hi + lo ) // 2
            root = TreeNode(nums[mid])
            root.left = build(lo, mid)
            root.right = build(mid+1, hi)
            return root
        return build(0, len(nums))