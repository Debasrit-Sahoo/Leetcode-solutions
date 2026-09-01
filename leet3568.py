class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom[0]), len(classroom)
        litter_id = [[-1] * m for _ in range(n)]
        c = 0
        start = None
        for x in range(n):
            for y in range(m): 
                if classroom[x][y] == 'L':
                    litter_id[x][y] = c
                    c += 1
                elif not start and classroom[x][y] == 'S':
                    start = (x, y)

        end = (1 << c) - 1
        
        best = [[[-1] * (1 << c) for _ in range(m)] for _ in range(n)]

        q = deque([(start[0], start[1], energy, 0)])

        moves = 0

        while q:
            for _ in range(len(q)):
                x, y, rem_e, mask = q.popleft()
                state = classroom[x][y]

                if state == 'L': 
                    mask |= 1 << litter_id[x][y]
                elif state == 'R': 
                    rem_e = energy

                if mask == end: return moves

                if best[x][y][mask] >= rem_e or not rem_e: continue
                best[x][y][mask] = rem_e

                rem_e -= 1
                if x - 1 >= 0 and classroom[x - 1][y] != 'X': q.append((x-1, y, rem_e, mask))
                if x + 1 < n and classroom[x + 1][y] != 'X': q.append((x+1, y, rem_e, mask))
                if y - 1 >= 0 and classroom[x][y - 1] != 'X': q.append((x, y-1, rem_e, mask))
                if y + 1 < m and classroom[x][y + 1] != 'X': q.append((x, y+1, rem_e, mask))

            moves += 1

        return -1