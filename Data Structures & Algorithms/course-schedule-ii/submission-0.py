from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegrees = [0] * numCourses

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegrees[course] += 1

        bfs = deque()

        for course, degree in enumerate(indegrees):
            if degree == 0:
                bfs.appendleft(course)

        courses = []
        while bfs:
            course = bfs.pop()

            courses.append(course)

            for neighbour in adj_list[course]:
                indegrees[neighbour] -= 1
                if indegrees[neighbour] == 0:
                    bfs.appendleft(neighbour)

        return [] if len(courses) != numCourses else courses

                