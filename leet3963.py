class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        if n == 1:
            return ['.' for i in range(m)]
        if m == 1:
            return ['.' * n]

        ans = ['.' + '#' + '.' * (n - 2) for _ in range(m - 2)]
        ans.append('.' + '#' * (n - 1))
        ans.append('.' * n)

        return ans