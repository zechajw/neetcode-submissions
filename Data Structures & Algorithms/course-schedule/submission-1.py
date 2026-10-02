
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses

        adj_list = defaultdict(list)

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegrees[course] += 1

        bfs = deque()
        for course, degree in enumerate(indegrees):
            if degree == 0:
                bfs.appendleft(course)

        courses = 0
        while bfs:
            course = bfs.pop()

            courses += 1
            for neighbour in adj_list[course]:
                indegrees[neighbour] -= 1
                if indegrees[neighbour] == 0:
                    bfs.appendleft(neighbour)

        return courses == numCourses