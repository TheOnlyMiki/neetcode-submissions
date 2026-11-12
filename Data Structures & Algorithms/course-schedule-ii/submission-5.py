class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        题目：共有 numCourses 门课，prerequisites[i] = [a, b] 表示学 a 之前必须先学 b。
             返回一种能学完所有课程的学习顺序；如果不可能学完，返回空列表。
        思路：拓扑排序（Kahn 算法，BFS），和 LeetCode 207（课程表）完全一样，
             只是把每门"可以学的课"按顺序记录下来，这个顺序就是拓扑序。
        - 入度 = 还没学完的先修课数量；入度为 0 的课可以直接学
        - 学完一门课，就把它的后续课程入度减 1；减到 0 就可以学
        - 图中有环时，环上的课程入度永远降不到 0，不会出现在 output 中
        例：numCourses = 4，prerequisites = [[1,0],[2,0],[3,1],[3,2]]
            0 → 1 → 3
              ↘ 2 ↗
            第 1 层：[0]，第 2 层：[1, 2]，第 3 层：[3]
            输出 [0, 1, 2, 3]（[0, 2, 1, 3] 也是合法答案）
        时间复杂度 O(V + E)：每个课程、每条先修关系各处理一次
        空间复杂度 O(V + E)：邻接表、入度数组、结果列表

        小提示：
        - 最后的判断也可以写成 len(output) == numCourses：
          学完的课程数等于总数就说明无环，不需要再对 indegree 求和，更直观。
              return output if len(output) == numCourses else []
        - 拓扑序不唯一，同一层内的课程可以任意交换顺序，题目接受任意一种。
        - DFS 也能求拓扑序：三色标记判环，节点在"所有后续节点都处理完"后加入结果（后序），
          最后把结果反转就是拓扑序。BFS 写法更直观，也不用担心递归深度。
        - 如果要求"字典序最小"的拓扑序，把队列换成最小堆即可。
        - 同类拓扑排序题：LeetCode 269（火星词典）、310（最小高度树，从叶子一层层剥）、
          1136（平行课程，按层数统计学期数）。
        """

        # indegree[c]：课程 c 还有几门先修课没学完
        indegree = [0] * numCourses

        # 邻接表：maps[b] 是以 b 为先修课的所有课程
        maps = [[] for i in range(numCourses)]

        # ---------- 第 1 步：建图并统计入度 ----------
        for course, pre in prerequisites:
            indegree[course] += 1       # course 多了一门先修课
            maps[pre].append(course)    # 边 pre → course

        # ---------- 第 2 步：没有先修课的课程作为第一层 ----------
        level = []

        for course in range(numCourses):
            if indegree[course] == 0:
                level.append(course)

        output = []   # 学习顺序（拓扑序）

        # ---------- 第 3 步：逐层学课，记录顺序并解锁后续课程 ----------
        while level:
            next_level = []

            for course in level:
                # 这门课的先修课都已学完，加入学习顺序
                output.append(course)

                # 学完 course，它的后续课程都少了一门先修课
                for next_course in maps[course]:

                    indegree[next_course] -= 1

                    # 先修课全部学完，下一轮可以学
                    if indegree[next_course] == 0:
                        next_level.append(next_course)

            level = next_level

        # 所有课程入度都降到 0 → 无环，output 就是完整的学习顺序
        # 否则存在环，无法学完所有课程
        if sum(indegree) == 0:
            return output
        else:
            return []