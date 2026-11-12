class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses
        maps = [[] for i in range(numCourses)]

        for start, end in prerequisites:
            indegree[end] += 1
            maps[start].append(end)

        level = []

        for course in range(numCourses):
            if indegree[course] == 0:
                level.append(course)

        while level:
            next_level = []

            for course in level:
                for prerequisite in maps[course]:
                    indegree[prerequisite] -= 1

                    if indegree[prerequisite] == 0:
                        next_level.append(prerequisite)

            level = next_level

        return sum(indegree) == 0
