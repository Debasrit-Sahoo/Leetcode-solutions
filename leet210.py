from collections import defaultdict
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        courses_taken = set(range(numCourses))
        for i in prerequisites:
            x = i[0]
            if x in courses_taken: courses_taken.remove(x)
            graph[x].append(i[1])
        order = list(courses_taken)
        change = True
        while change:
            change = False
            for course, dependancies in list(graph.items()):
                temp = [d for d in dependancies if d not in courses_taken]
                if not temp:
                    courses_taken.add(course)
                    order.append(course)
                    change = True
                    del graph[course]
                else:
                    graph[course] = temp
        if len(order) == numCourses:
            return order
        return []