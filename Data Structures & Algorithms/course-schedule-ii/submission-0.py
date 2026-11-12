class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses
        maps = [[] for i in range(numCourses)]

        for start, end in prerequisites:
            indegree[end] += 1
            maps[start].append(end)

        level = []

        for course in range(numCourses):
            if indegree[course] == 0:
                level.append(course)

        output = []

        while level:
            next_level = []

            for course in level:
                output.append(course)

                for prerequisite in maps[course]:

                    indegree[prerequisite] -= 1

                    if indegree[prerequisite] == 0:
                        next_level.append(prerequisite)

            level = next_level

        if sum(indegree) == 0:
            return output[::-1]
        else:
            return []