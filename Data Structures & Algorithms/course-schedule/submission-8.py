class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        course_prerequisite = [0] * numCourses
        maps = [[] for i in range(numCourses)]

        for course, pre in prerequisites:
            course_prerequisite[course] += 1
            maps[pre].append(course)

        level = []

        for i in range(len(course_prerequisite)):
            if course_prerequisite[i] == 0:
                level.append(i)

        output = 0

        while level:
            next_level = []

            for course in level:
                output += 1

                for next_course in maps[course]:
                    course_prerequisite[next_course] -= 1
                    if course_prerequisite[next_course] == 0:
                        next_level.append(next_course)

            level = next_level

        return output == numCourses
