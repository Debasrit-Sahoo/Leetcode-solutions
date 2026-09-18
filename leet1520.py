class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        intervals = [None] * 26
        ans = []

        off = ord('a')

        for i, c in enumerate(s):
            idx = ord(c) - off

            if intervals[idx]:
                intervals[idx][1] = i
            else:
                intervals[idx] = [i, i]

        for each in intervals:
            if not each:
                continue

            left, right = each
            j = left

            while j <= right:
                first, last = intervals[ord(s[j]) - off]

                if first < left: break
                if last > right: right = last

                j += 1
            else:
                ans.append((left, right))

        intervals = sorted(ans, key=lambda x: x[1])

        p = -1
        ans = []

        for start, end in intervals:
            if start > p:
                p = end
                ans.append(s[start:end+1])

        return ans