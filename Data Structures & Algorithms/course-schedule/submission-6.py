class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        record = {}
        for course, pre in prerequisites:
            if course in record:
                record[course].append(pre)
            else:
                record[course] = [pre]

        register = set()

        def checkCourseBeenTaken(course):
            # If the course is not planning to take, then no matter
            if course not in record:
                return True

            # If the course already been taken, it means conflict
            if course in register:
                return False

            # If the course has no conflict then register/taken
            register.add(course)

            # Check the pre require courses is conflict or not (And register when we check)
            for pre in record[course]:
                if not checkCourseBeenTaken(pre):
                    return False

            # If the course and pre require courses all register, then clear the whole list from record
            del record[course]

            return True

        for course in range(numCourses):
            if not checkCourseBeenTaken(course):
                return False

        return True

        """
        题目：共有 numCourses 门课（编号 0 ~ numCourses-1），
             prerequisites[i] = [a, b] 表示学 a 之前必须先学 b。判断能否学完所有课程。
        思路：拓扑排序（Kahn 算法，BFS）
        - 把课程看成有向图：b → a 表示 b 是 a 的先修课
        - 能学完所有课 ⇔ 图中没有环（有环就互相等待，谁都学不了）
        - 入度 = 还没学完的先修课数量；入度为 0 的课可以直接学
        - 每学完一门课，就把它指向的后续课程入度减 1；某门课入度减到 0，就可以学了
        - 最后如果所有课程的入度都变成 0，说明都学完了；有剩余说明存在环
        例：numCourses = 4，prerequisites = [[1,0],[2,1],[3,1]]
            0 → 1 → 2
                  ↘ 3
            第 1 层：[0]，第 2 层：[1]，第 3 层：[2, 3]，全部学完 → True
            若再加 [0,2]：0 → 1 → 2 → 0 形成环，三门课入度都无法降到 0 → False
        时间复杂度 O(V + E)：V 为课程数，E 为先修关系数，每个点、每条边各处理一次
        空间复杂度 O(V + E)：邻接表和入度数组

        小提示：
        - 判断条件 sum(indegree) == 0 也可以换成"统计学完的课程数是否等于 numCourses"：
          每次课程入队时 count += 1，最后 return count == numCourses。
          环上的课程入度永远不会降到 0，所以两种判断等价。
        - 这里按层处理（level / next_level），其实本题不需要层的信息，
          用一个普通队列或栈都可以；但按层写的话，层数就是"最少需要几个学期"
          （LeetCode 1136 平行课程）。
        - DFS 写法：三色标记法，0 = 未访问，1 = 正在当前递归路径上，2 = 已确认无环。
          DFS 过程中遇到状态为 1 的节点，说明回到了当前路径上 → 有环。
        - LeetCode 210（课程表 II）：同样的代码，把每次可以学的课依次加入结果列表，
          最后若长度等于 numCourses 就返回这个顺序（即拓扑序），否则返回空列表。
        """

        # indegree[c]：课程 c 还有几门先修课没学完
        indegree = [0] * numCourses

        # 邻接表：maps[b] 是以 b 为先修课的所有课程（b 学完后可以解锁它们）
        maps = [[] for i in range(numCourses)]

        # ---------- 第 1 步：建图并统计入度 ----------
        for course, pre in prerequisites:
            indegree[course] += 1       # course 多了一门先修课
            maps[pre].append(course)    # 边 pre → course

        # ---------- 第 2 步：没有先修课的课程可以直接学，作为第一层 ----------
        level = []

        for course in range(numCourses):
            if indegree[course] == 0:
                level.append(course)

        # ---------- 第 3 步：逐层"学课"，解锁后续课程 ----------
        while level:
            next_level = []

            for course in level:
                # 学完 course，它的后续课程都少了一门先修课
                for next_course in maps[course]:
                    indegree[next_course] -= 1

                    # 先修课全部学完，下一轮就可以学这门课
                    if indegree[next_course] == 0:
                        next_level.append(next_course)

            level = next_level

        # 所有课程入度都降到 0 → 都学完了；否则剩下的课程处在环中
        return sum(indegree) == 0