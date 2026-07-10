class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sorted_nodes = [(v, i) for i, v in enumerate(nums)]
        sorted_nodes.sort()
        LOG = n.bit_length()
        comp = [0]*n
        pos = [0]*n
        jump = [[-1]*n for _ in range(LOG)]
        j = 0
        c = 0
        for i in range(n):
            if i > j: j = i
            value, node = sorted_nodes[i]
            pos[node] = i
            comp[node] = c
            v = value + maxDiff
            while j + 1 < n and sorted_nodes[j + 1][0] <= v: j += 1
            if i == j: c += 1
            jump[0][i] = j

        for k in range(1, LOG):
            for i in range(n):
                jump[k][i] = jump[k-1][jump[k-1][i]]

        for i, (start, end) in enumerate(queries):
            if start == end:
                queries[i] = 0
            elif comp[start] != comp[end]:
                queries[i] = -1
            else:
                if nums[start] > nums[end]:
                    start, end = end, start

                cost = 0
                cur = pos[start]
                end = pos[end]
                for k in range(LOG - 1, -1, -1):
                    if jump[k][cur] < end:
                        cur = jump[k][cur]
                        cost += 1 << k

                queries[i] = cost + 1
            
        return queries