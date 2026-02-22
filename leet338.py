class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]*(n+1)
        for i in range(1,n+1):
            arr[i] = arr[i>>1] + (i&1)
        return arr