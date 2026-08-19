class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        LEFT  = 0b0000111100
        MID   = 0b0011110000
        RIGHT = 0b1111000000

        rows = defaultdict(int)

        for row, seat in reservedSeats:
            rows[row] |= 1 << seat

        acc = (n - len(rows)) << 1

        for s in rows.values():
            left = not (s & LEFT)
            right = not (s & RIGHT)

            if left and right:
                acc += 2
            elif left or right or not (s & MID):
                acc += 1

        return acc