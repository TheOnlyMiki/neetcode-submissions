class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

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

        # 思路：DFS 判断有向图里有没有环（三色标记）。
        #   没有环 → 所有课都能上完；有环 → 存在循环依赖，上不完。
        #
        # 三种状态用两个结构的组合来表示：
        #   在 record 里、不在 visiting 里 → 未访问
        #   在 record 里、也在 visiting 里 → 访问中（在当前 DFS 路径上）
        #   不在 record 里                → 已完成（确认没有环，或者本来就没有先修课）

        # record[course] = course 的所有先修课
        # 小提示：defaultdict(list) 访问不存在的 key 时会自动创建空列表，
        #   省掉 if course in record / else 的判断
        record = defaultdict(list)
        for course, pre in prerequisites:
            record[course].append(pre)

        # 当前这条 DFS 依赖链上的课
        visiting = set()

        def canTake(course):
            # 不在 record 里，有两种可能：
            #   1. 这门课本来就没有先修课
            #   2. 之前已经检查过，它和它的所有先修课都没有环
            # 两种情况都说明这门课一定能上
            # 小提示：这个判断必须放在 visiting 判断前面。
            #   visiting 里的元素从不删除，如果顺序反过来，已完成的课会被误判成环
            # 小提示：对 defaultdict 做 "in" 判断不会创建新 key，只有 record[x] 取值才会，
            #   所以这里是安全的
            if course not in record:
                return True

            # 还没检查完，却又在当前依赖链上出现了一次，
            # 说明依赖链绕回了自己，比如 A → B → C → A，存在环
            if course in visiting:
                return False

            # 标记为"访问中"，然后递归检查它的每一门先修课
            visiting.add(course)
            for pre in record[course]:
                if not canTake(pre):
                    return False

            # 所有先修课都检查完了，没有环。
            # 从 record 删掉，标记为"已完成"
            # 小提示：这一步相当于记忆化。以后别的课再依赖它，会在第一个 if 直接返回 True，
            #   保证每门课只被完整检查一次，总复杂度 O(V + E)
            del record[course]
            return True

        # 每门课都检查一遍，只要有一门课处在环里就返回 False
        # 小提示：all() 遇到第一个 False 就会停止，和原来的 for 循环 + return False 等价
        return all(canTake(course) for course in range(numCourses))

        # 小提示：时间复杂度 O(V + E)，空间复杂度 O(V + E)。V 是课程数，E 是先修关系数
        # 小提示：最坏递归深度等于最长依赖链的长度，题目上限是 2000，超过了 Python 默认的 1000 层。
        #   LeetCode 环境一般能过；在别的环境里可以在开头加上 sys.setrecursionlimit(10000)，
        #   或者改用 BFS 拓扑排序（Kahn 算法），完全避开递归
        