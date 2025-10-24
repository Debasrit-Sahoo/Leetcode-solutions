def canJump(nums):
        lim = 0
        for i,v in enumerate(nums):
            if i > lim:
                return False
            lim = lim if i + v < lim else i + v
        return True