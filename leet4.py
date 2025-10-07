def findMedianSortedArrays(a,b):
        if len(a) > len(b):
            a, b = b, a
        A = [float("-inf")] + a + [float("inf")]
        B = [float("-inf")] + b + [float("inf")]
        total = len(a) + len(b) 
        half = total // 2
        l = 1
        h = len(a)
        while True:
            P1 = ( l + h ) // 2
            P2 = half - P1
            A_left = A[P1]
            A_right = A[P1 + 1]
            B_left = B[P2]
            B_right = B[P2 + 1]
            if A_left > B_right:
                h = P1 - 1
                continue
            if B_left > A_right:
                l = P1 + 1
                continue
            if total % 2:
                return min(A_right, B_right)
            return (max(A_left, B_left) + min(A_right, B_right)) / 2