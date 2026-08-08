class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        m = r - l 
        r += 1
        size = r - l
        k = n - 2
        
        fx = np.fliplr(np.triu(np.ones((m , m), dtype=object)))

        seed = [0] * (size)
        for i in range(1, size):
            seed[i] = (seed[i-1] + size - i) % MOD
        seed = seed[1:][::-1]

        seed = np.array(seed, dtype=object)

        res = np.eye(m, dtype=object)

        while k > 0:
            if k & 1:
                res = (res @ fx) % MOD
            fx = (fx @ fx) % MOD
            k >>= 1

        ans = (res @ seed) % MOD
        return int(ans[0] << 1) % MOD 