class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        parent = [i for i in range(n)]
        size = [1] * n

        def find(i):
            boss = i
            while parent[boss] != boss:
                boss = parent[boss]

            while parent[i] != boss:
                parent[i], i = boss, parent[i]

            return boss

        def union(a, b):
            boss_a, boss_b = find(a), find(b)

            if boss_a == boss_b:
                return True

            if size[boss_a] < size[boss_b]:
                boss_a, boss_b = boss_b, boss_a
            parent[boss_b] = boss_a
            size[boss_a] += size[boss_b]

            return False

        for a, b in edges:
            if union(a, b):
                return False

        if max(size) != n:
            return False

        return True
































        """
        题目：n 个节点（编号 0 ~ n-1）和一组无向边 edges，判断这些边能否构成一棵有效的树。
        树的判定：一张无向图是树 ⇔ 满足以下任意两条（第三条自动成立）
            1. 连通（所有节点能互相到达）
            2. 无环
            3. 边数恰好为 n - 1
        两种方法都利用"边数 = n - 1"，再检查另一条：
        - Method 2 并查集：边数 = n - 1 + 无环
        - Method 1 BFS   ：边数 = n - 1 + 连通
        例：n = 5，edges = [[0,1],[0,2],[0,3],[1,4]] → True
            n = 5，edges = [[0,1],[1,2],[2,3],[1,3],[1,4]] → False（1-2-3 成环）
        时间复杂度：并查集 O(n + E · α(n))，α 为反阿克曼函数，可视为常数；BFS O(n + E)
        空间复杂度 O(n + E)

        小提示：
        - 原并查集写法漏了边数检查：只判断了"无环"，没判断"连通"。
          例如 n = 4，edges = [[0,1]]：没有环，会返回 True，但 2、3 是孤立点，不是树。
          已在开头补上 if len(edges) != n - 1: return False。
          边数为 n - 1 且无环 ⇒ 一定连通，所以补上这一句后结论就完整了。
        - 边数检查放在最前面还是一个优化：边数不对直接返回，省掉后面所有计算。
        - 路径压缩里的 parent[x], x = root, parent[x]：
          Python 会先算出右边的 (root, parent[x])，再依次赋值，
          所以 parent[x] 被改成 root 时，x 拿到的是"改之前"的上级，能继续往上走。
        - 按大小合并 + 路径压缩一起用，单次操作均摊接近 O(1)；
          只用其中一个也能过题，但面试时两个都写出来是加分项。
        - 并查集模板还可以用于：LeetCode 323（无向图连通分量数）、547（省份数量）、
          684（冗余连接：返回第一条让 find(a) == find(b) 的边）、
          200（岛屿数量的并查集解法）。
        """

        # ==================== Method 2 - 并查集（Union-Find） ====================

        # 树的边数必须恰好是 n - 1：少了一定不连通，多了一定有环
        if len(edges) != n - 1:
            return False

        parent = list(range(n))  # parent[i] = i 的上级，初始每个人自己是老大
        size = [1] * n           # size[老大] = 这个团体有几个人

        def find(x):
            """返回 x 所在团体的老大（根节点）"""
            # 先一路往上找到老大
            root = x
            while parent[root] != root:
                root = parent[root]
            # 路径压缩：再走一遍，把沿途每个人的上级都直接改成老大
            # 这一步不影响正确性，只是让以后的 find 更快
            while parent[x] != root:
                parent[x], x = root, parent[x]
            return root

        for a, b in edges:
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                return False  # 已经连通，再加边就是环

            # 按大小合并：保证 root_a 是人多的那一边，再把 root_b 挂到它下面
            # 小团体挂到大团体下，树高增长更慢，find 更快
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            parent[root_b] = root_a
            size[root_a] += size[root_b]

        # 边数为 n - 1 且没有环 → 一定连通 → 是树
        return True

        # ==================== Method 1 - 边数检查 + BFS 判断连通 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留

        # 边数不是 n - 1，一定不是树
        if len(edges) != n-1:
            return False

        # 无向图邻接表：每条边两个方向都要加
        maps = [[] for i in range(n)]

        for a,b in edges:
            maps[a].append(b)
            maps[b].append(a)

        # 从节点 0 出发 BFS，统计能到达多少个节点
        level = [0]

        visit = {0}

        while level:
            next_level = []

            for node in level:
                for next_node in maps[node]:

                    # 没访问过的邻居加入下一层
                    # （无向图中父节点也在邻居列表里，靠 visit 跳过，不会走回头路）
                    if next_node not in visit:
                        visit.add(next_node)
                        next_level.append(next_node)

            level = next_level

        # 能到达所有节点 → 连通；再加上边数为 n - 1 → 是树
        return len(visit) == n