class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        course_prerequisite = [0] * numCourses
        
        maps = [[] for i in range(numCourses)]

        for course, pre in prerequisites:
            course_prerequisite[course] += 1
            maps[pre].append(course)

        level = []

        for i in range(numCourses):
            if course_prerequisite[i] == 0:
                level.append(i)

        output = []

        while level:
            next_level = []

            for course in level:
                output.append(course)

                for next_course in maps[course]:
                    course_prerequisite[next_course] -= 1
                    if course_prerequisite[next_course] == 0:
                        next_level.append(next_course)

            level = next_level

        return output if len(output) == numCourses else []
