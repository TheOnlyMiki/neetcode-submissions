class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses
        maps = [[] for i in range(numCourses)]

        for start, end in prerequisites:
            indegree[start] += 1
            maps[end].append(start)

        level = []

        for course in range(numCourses):
            if indegree[course] == 0:
                level.append(course)

        output = []

        while level:
            next_level = []

            for course in level:
                output.append(course)

                for next_course in maps[course]:

                    indegree[next_course] -= 1

                    if indegree[next_course] == 0:
                        next_level.append(next_course)

            level = next_level

        if sum(indegree) == 0:
            return output
        else:
            return []