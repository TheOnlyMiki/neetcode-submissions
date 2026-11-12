class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        题目：给定机票列表 tickets[i] = [from, to]，从 "JFK" 出发，必须用完所有机票且每张只用一次。
             若有多种行程，返回字典序最小的那个。题目保证至少存在一种合法行程。
        本质：在有向图中找一条从 JFK 出发、经过每条边恰好一次的路径 → 欧拉路径（一笔画）
        三种方法：
        - Method 3 / 2：Hierholzer 算法（迭代 / 递归），O(E log E)
        - Method 1：回溯，按字典序尝试，第一个用完所有机票的路径就是答案，最坏指数级

        Hierholzer 为什么要"反向"：
        - 每次贪心地走字典序最小的边，并把用过的边删掉
        - 走到某个机场没有出边可走（卡住）时，把它加入结果，然后退回上一个机场继续走
        - 先卡住的机场一定在行程的最后面，所以结果是倒着收集的，最后反转
        例：tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
            JFK 的目的地按字典序：KUL < NRT
            JFK → KUL，KUL 没有出边，卡住 → 结果 [KUL]
            退回 JFK → NRT → JFK，JFK 没有出边了，卡住 → 结果依次加入 JFK、NRT、JFK
            结果 [KUL, JFK, NRT, JFK]，反转 → [JFK, NRT, JFK, KUL]
            若直接按贪心顺序输出 [JFK, KUL, ...] 会卡在 KUL 用不完机票，这就是"反向收集"的意义：
            走进死胡同的那段（KUL）被自动放到行程最后，别的环（JFK → NRT → JFK）插在它前面

        小提示：
        - 每个机场的目的地按字典序"倒序"排列，这样 pop() 从末尾取出的就是字典序最小的，
          每次删除都是 O(1)；如果正序排列再 pop(0)，每次删除是 O(n)。
          也可以用最小堆存每个机场的目的地，heappop 取最小的。
        - Method 3 里 cur = "JFK" 那一行可以删掉，循环里会重新赋值。
        - Method 3 是 Method 2 的迭代版：显式栈 s 模拟递归调用栈，
          栈顶还有出边就"递归"（入栈），没有出边就"返回"（出栈并加入结果）。
          机票数量多时不用担心递归深度超限。
        - Method 1 的去重：同一个机场有多张飞往同一目的地的机票时，它们完全等价，
          同一层只需尝试第一张没用过的。和 LeetCode 47（全排列 II）的同层去重条件一样。
        - Method 1 能找到答案是因为"按字典序尝试 + 第一个成功就返回"，
          但遇到死胡同要回退，最坏指数级时间；LeetCode 后来加了专门卡回溯的测试用例，可能会超时。
          面试中先说回溯思路可以，但最好能讲出 Hierholzer。
        - 欧拉路径存在的条件（有向图）：起点出度 - 入度 = 1，终点入度 - 出度 = 1，其余节点出入度相等
          （或所有节点出入度都相等，此时是欧拉回路）。本题保证存在，所以不用检查。
        - 同类题：LeetCode 753（破解保险箱，构造 de Bruijn 序列，也是欧拉回路）、
          2097（合法重新排列数对，欧拉路径但起点需要自己找）。
        """

        # ==================== Method 3 - Hierholzer 迭代（显式栈，反向收集） ====================
        # 时间复杂度 O(E log E)：排序为主，每条边只走一次
        # 空间复杂度 O(E)：邻接表、栈、结果

        output = []                 # 倒序收集的行程
        edges = defaultdict(list)   # 机场 → 目的地列表

        # ---------- 第 1 步：建图 ----------
        for src, dst in tickets:
            edges[src].append(dst)

        # 倒序排列，pop() 取出的是字典序最小的目的地
        for values in edges.values():
            values.sort(reverse=True)

        # ---------- 第 2 步：模拟 DFS ----------
        s = ["JFK"]   # 当前正在走的路径（相当于递归调用栈）
        cur = "JFK"

        while s:
            cur = s[-1]

            # 还有没用的机票：沿字典序最小的那张继续走（相当于递归进入下一层）
            if edges[cur]:
                s.append(edges[cur].pop())

            # 没有机票可用了（卡住）：这个机场放在当前剩余行程的最后
            # 出栈并加入结果（相当于递归返回时记录）
            else:
                output.append(s.pop())

        # 收集顺序是从行程末尾往前，反转后得到正确行程
        return output[::-1]

        # ==================== Method 2 - Hierholzer 递归（后序收集） ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(E log E)，空间复杂度 O(E)（递归深度最多 E）

        maps = defaultdict(list)

        # 整体倒序排序后依次加入，每个机场的目的地列表自然是倒序的
        for from_i, to_i in sorted(tickets, reverse=True):
            maps[from_i].append(to_i)

        path = []   # 后序收集的行程（倒序）

        def dfs(from_i):
            # 把当前机场所有机票用完：每次取字典序最小的目的地递归
            # 用 while 而不是 for：递归回来后，当前机场可能还有别的机票没用（别的环）
            while maps[from_i]:
                to_i = maps[from_i].pop()   # 用掉这张机票（删除边）
                dfs(to_i)

            # 当前机场再也没有出边，所有从这里出发的行程都已安排好
            # 后序位置加入：它在剩余行程中排在最后
            path.append(from_i)

        dfs("JFK")

        # 后序收集是倒序的，反转得到正确行程
        return path[::-1]

        # ==================== Method 1 - 回溯 ====================
        # 时间复杂度：最坏指数级（遇到死胡同需要回退重试）
        # 空间复杂度 O(E)：邻接表、path、递归深度
        # 思路：按字典序依次尝试每张没用过的机票，用完所有机票就找到答案；
        #      走进死胡同就撤销选择，换下一张机票

        maps = defaultdict(list)

        # 正序排序：按字典序从小到大尝试，第一个成功的就是字典序最小的行程
        # 每张机票记录为 [目的地, 是否已使用]
        for from_i, to_i in sorted(tickets):
            maps[from_i].append([to_i, False])

        n = len(tickets)

        path = ["JFK"]   # 当前行程

        def backtrack(from_i):
            """从 from_i 出发，尝试用完剩余机票；成功返回 True"""
            # 行程有 n + 1 个机场 = 用完了 n 张机票
            if len(path) == n+1:
                return True

            for i, (to_i, visit) in enumerate(maps[from_i]):
                # 这张机票已经用过
                if visit:
                    continue

                # 同层去重：和前一张机票目的地相同，且前一张没用过（本层已经试过它）
                # 两张机票等价，再试一次结果一样；删掉不影响结果，但能减少重复分支
                if i > 0 and to_i == maps[from_i][i-1][0] and not maps[from_i][i-1][1]:
                    continue

                # 做选择：使用这张机票
                path.append(to_i)
                maps[from_i][i][1] = True

                # 后面能用完所有机票，就是答案（按字典序第一个成功的），层层返回
                if backtrack(to_i):
                    return True

                # 撤销选择：这条路走不通，换下一张机票
                maps[from_i][i][1] = False
                path.pop()

            # 所有机票都试过了，从这里走不通
            return False

        backtrack("JFK")

        return path