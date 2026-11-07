class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        freeheap = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(freeheap)
        utilheap = []

        push = heapq.heappush
        pop = heapq.heappop

        time = 0
        for i, t in enumerate(tasks):
            if i > time: time = i
            if not freeheap and utilheap[0][0] > time:
                time = utilheap[0][0]
            while utilheap and time >= utilheap[0][0]:
                push(freeheap, pop(utilheap)[1:])

            s = pop(freeheap)
            push(utilheap, (t + time,) + s)
            tasks[i] = s[1]

        return tasks