class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        题目：网络中有 n 个节点（编号 1 ~ n），times[i] = (u, v, w) 表示信号从 u 传到 v 需要 w 时间（有向边）。
             从节点 k 发出信号，求所有节点都收到信号的最短时间；有节点收不到则返回 -1。
        思路：单源最短路。先求 k 到每个节点的最短距离，答案就是其中的最大值
             （所有节点都收到 = 最晚收到的那个节点也收到了）。
             边权都是非负数 → 可以用 Dijkstra；也可以用通用的 Bellman-Ford。
        例：times = [[2,1,1],[2,3,1],[3,4,1]]，n = 4，k = 2
            2 → 1（1）
            2 → 3（1）→ 4（2）
            最短距离：节点 1 为 1，节点 3 为 1，节点 4 为 2 → 答案 2

        小提示：
        - 三种方法对比（V 为节点数 n，E 为边数）：
          · Method 3 Bellman-Ford：O(V · E)，写法最短，支持负权边（本题没有负权）
          · Method 2 / 1 Dijkstra（堆优化）：O(E log E)，只适用于非负权边，本题首选
        - Dijkstra 的核心性质：边权非负时，从堆里第一次弹出某个节点，此时的距离就是它的最短距离，
          之后再弹出同一个节点（更长的距离）直接跳过。这叫"懒删除"：
          不去更新堆里已有的元素，而是允许重复入堆，弹出时再过滤。
        - Method 2 在 visit 满 n 个时直接返回 t：Dijkstra 按距离从小到大确定节点，
          最后一个被确定的节点距离最大，正好就是答案，不用再求 max。
        - Method 1 写了 min_heap = maps[k]，这不是复制，而是和邻接表 maps[k] 共用同一个列表，
          之后的 heapify / heappush / heappop 都会改动 maps[k]。
          这里碰巧没出错（k 一开始就在 visit 中，maps[k] 不会再被当作邻接表遍历），
          但很容易埋 bug，应改成 min_heap = list(maps[k]) 复制一份。
        - Bellman-Ford 的优化：某一轮没有任何距离被更新，说明已经收敛，可以提前结束, 再做第 n 轮松弛如果仍能更新，说明图中有负权环（Bellman-Ford 可以检测负环，Dijkstra 不行）。
        - 同类最短路题：LeetCode 787（K 站中转内最便宜的航班，限制边数 → Bellman-Ford 只跑 K+1 轮）、
          1514（概率最大的路径，Dijkstra 改成最大堆）、1631（最小体力消耗路径，网格上的 Dijkstra）。
        """

        # ==================== Method 3 - Bellman-Ford ====================
        # 时间复杂度 O(V · E)，空间复杂度 O(V)
        # 思路：反复"松弛"所有边：若经过 u 到 v 更近，就更新 dist[v]
        #      最短路径最多包含 n - 1 条边，所以松弛 n - 1 轮后一定得到所有最短距离

        # dist[i]：从 k 到节点 i 的最短距离；节点编号从 1 开始，多开一位
        dist = [float('inf')] * (n+1)
        dist[0] = 0   # 下标 0 不是真实节点，设为 0 避免影响最后求 max
        dist[k] = 0   # 起点到自己距离为 0

        # 松弛 n - 1 轮
        for _ in range(n - 1):
            # Bellman-Ford 的优化：某一轮没有任何距离被更新，说明已经收敛，可以提前结束
            updated = False
            for u, v, w in times:
                # u 已经可达，且经过 u 到 v 比当前记录更近
                # （dist[u] 为 inf 时 inf + w 仍是 inf，不会误更新）
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True

            # 某一轮没有任何距离被更新，说明已经收敛，可以提前结束
            if not updated:
                    break

        # 最晚收到信号的节点
        max_dist = max(dist)

        # 仍为 inf 说明有节点不可达
        return max_dist if max_dist < float('inf') else -1

        # ==================== Method 2 - Dijkstra（堆优化，集齐 n 个即返回） ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(E log E)：每条边最多让一个元素入堆
        # 空间复杂度 O(V + E)：邻接表和堆
        # 思路：每次从堆中取出"当前距离最小且还没确定"的节点，确定它的最短距离，
        #      再用它去更新邻居的距离（邻居带着新距离入堆）

        # 邻接表：maps[u] = [(边权, 终点), ...]
        maps = [[] for i in range(n+1)]

        for u, v, t in times:
            maps[u].append((t, v))

        # 堆中元素为 (从 k 出发的距离, 节点)，按距离排序
        min_heap = [(0, k)]

        visit = set()   # 已确定最短距离的节点

        while min_heap:
            t, v = heapq.heappop(min_heap)

            # 已经确定过（之前弹出的是更短的距离），这是过期的记录，跳过
            if v in visit:
                continue

            # 第一次弹出：t 就是 k 到 v 的最短距离
            visit.add(v)

            # 所有节点都已确定：最后确定的节点距离最大，就是答案
            if len(visit) == n:
                return t

            # 用 v 更新邻居：经过 v 到达邻居的距离入堆
            for next_t, next_v in maps[v]:
                heapq.heappush(min_heap, (t + next_t, next_v))

        # 堆空了还没确定完所有节点，说明有节点不可达
        return -1

        # ==================== Method 1 - Dijkstra（堆优化，先把起点的邻居入堆） ====================
        # 时间复杂度 O(E log E)，空间复杂度 O(V + E)
        # 和 Method 2 相同，只是起点直接记录为距离 0，并把它的出边作为初始堆

        maps = [[] for i in range(n+1)]

        for u, v, t in times:
            maps[u].append((t, v))

        # 起点的所有出边作为初始候选：(边权, 终点) 恰好就是 (距离, 节点)
        # 注意：这里和 maps[k] 共用同一个列表，更稳妥的写法是 list(maps[k])
        min_heap = maps[k]

        heapq.heapify(min_heap)

        # 节点 → 最短距离；起点距离为 0
        visit = {k:0}

        while min_heap:
            t, v = heapq.heappop(min_heap)

            # 第一次弹出：确定 v 的最短距离
            if v not in visit:
                visit[v] = t

                # 只把还没确定的邻居入堆，减少无效元素
                for next_t, next_v in maps[v]:
                    if next_v not in visit:
                        heapq.heappush(min_heap, (t + next_t, next_v))

        # 有节点没被确定，说明不可达
        if len(visit) != n:
            return -1

        # 所有节点都收到信号的时间 = 最短距离中的最大值
        return max(visit.values())