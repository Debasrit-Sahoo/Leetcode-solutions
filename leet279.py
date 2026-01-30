class Solution:
    def numSquares(self, n: int) -> int:
        sq = [i*i for i in range(1, int(n**0.5)+1)]
        stack = deque([n])
        done = {n}
        lvl = 1
        while stack:
            for _ in range(len(stack)):
                x = stack.popleft()
                for s in sq:
                    a = x - s
                    if a < 0: break
                    if a == 0: return lvl
                    if a not in done: done.add(a); stack.append(a)
            lvl += 1