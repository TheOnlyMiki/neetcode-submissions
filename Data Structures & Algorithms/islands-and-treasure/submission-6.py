class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        m, n = len(grid), len(grid[0])

        level = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    level.append((i, j))

        while level:
            next_level = []

            for i, j in level:
                for a,b in [(1,0), (0,1),(-1,0),(0,-1)]:
                    x, y = i+a, j+b

                    if 0 <= x < m and 0 <= y < n and grid[x][y] > grid[i][j] + 1:
                        grid[x][y] = grid[i][j] + 1
                        next_level.append((x,y))

            level = next_level

        return



































        """
        题目：网格中 -1 表示水（不能通过），0 表示宝藏，INF（2147483647）表示陆地。
             把每块陆地的值改成它到最近宝藏的步数（上下左右移动），到不了的保持 INF。
             原地修改，不返回值。（即 LeetCode 286 墙与门）
        例：grid = [[INF, -1,   0, INF],
                    [INF, INF, INF, -1],
                    [INF, -1, INF, -1],
                    [  0, -1, INF, INF]]
            结果   [[  3, -1,   0,   1],
                    [  2,   2,   1, -1],
                    [  1, -1,   2, -1],
                    [  0, -1,   3,   4]]

        小提示：
        - 多源 BFS：可以想象成在所有宝藏处同时扔下石子，水波一圈一圈同步向外扩散，
          每个格子第一次被波纹碰到时，碰到它的一定是最近的那个宝藏。
        - BFS 按距离逐层扩展，第一次访问时就是最短距离，之后不会再变，
          所以 grid 本身就充当了 visited 数组（只扩展值仍为 INF 的格子），不需要额外的 set。
        - 不要对每个宝藏分别跑一次 BFS，那样是 O(k · m · n)（k 为宝藏数）。
          多源 BFS 一开始就把所有起点放进队列，只需要跑一遍。
        - Method 1 的 DFS 能得到正确答案，但效率差：DFS 先到达某格子时走的不一定是最短路，
          之后发现更短的路径还要再次更新并重新向外扩散，同一个格子可能被反复更新很多次；
          而且递归深度可能达到 m · n，有爆栈风险。求"最短距离"优先想到 BFS。
        - 同类多源 BFS 题：LeetCode 994（腐烂的橘子）、542（01 矩阵）、
          1162（地图分析）。思路都是"把所有起点同时入队，再一层层扩散"。
        """

        # ==================== Method 2 - 多源 BFS ====================
        # 时间复杂度 O(m · n)：每个格子最多入队、出队一次
        # 空间复杂度 O(m · n)：队列最坏存下所有格子；没有递归，不会爆栈

        inf_val = 2147483647

        m, n = len(grid), len(grid[0])

        # ---------- 第 1 步：所有宝藏同时作为起点入队 ----------
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        # ---------- 第 2 步：一层层向外扩散 ----------
        while q:
            i, j = q.popleft()
            for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x, y = i + a, j + b
                # 只扩展到还是 INF 的陆地；
                # 不是 INF 说明已经被更近的宝藏访问过，或者是水 / 宝藏本身
                if 0 <= x < m and 0 <= y < n and grid[x][y] == inf_val:
                    # 第一次到达，距离 = 来源格子的距离 + 1，就是最短距离
                    grid[x][y] = grid[i][j] + 1
                    q.append((x, y))

        return

        # ==================== Method 1 - 从每个宝藏出发 DFS，遇到更短路径就更新 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度：最坏远大于 O(m · n)，同一个格子可能被不同路径反复更新
        # 空间复杂度：递归深度最坏 O(m · n)
        # 思路：从每个宝藏出发往外走，每走一步距离 + 1，
        #      如果当前走到的距离比格子里记录的更小，就更新并继续往外走；否则剪枝

        m, n = len(grid), len(grid[0])

        def dfs(i, j, count):
            """
            (i, j)：当前格子
            count ：从出发的宝藏走到这里的步数
            """
            # 不越界，且是陆地（> 0；水是 -1，宝藏是 0，都不处理）
            if 0 <= i < m and 0 <= j < n and grid[i][j] > 0:
                # 找到更短的路径才更新，并继续向外扩散；
                # 否则说明已经有更近的宝藏覆盖了这里，再走下去也不会让别人更短，剪枝
                if grid[i][j] > count:
                    grid[i][j] = count
                    for a, b in [(1,0),(0,1),(-1,0),(0,-1)]:
                        dfs(i+a, j+b, count+1)

        # 从每个宝藏出发，向四个相邻格子开始 DFS（宝藏本身距离为 0，不需要更新）
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    for a, b in [(1,0),(0,1),(-1,0),(0,-1)]:
                        dfs(i+a, j+b, 1)

        return