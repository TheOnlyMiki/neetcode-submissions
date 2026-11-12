class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        inf_val = 2147483647

        m, n = len(grid), len(grid[0])

        # 把所有宝藏一起放进队列作为起点，这就是"多源 BFS"
        # 小提示：可以想象成在所有宝藏处同时扔下石子，水波一圈一圈同步向外扩散，
        #   每个格子第一次被波纹碰到时，碰到它的一定是最近的那个宝藏
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x, y = i + a, j + b
                # 只扩展到还是 INF 的陆地。不是 INF 说明已经被更近的宝藏访问过，
                # 或者是水或宝藏本身
                # 小提示：BFS 按距离逐层扩展，第一次访问时就是最短距离，之后不会再变，
                #   所以 grid 本身就充当了 visited 数组，不需要额外的 set
                if 0 <= x < m and 0 <= y < n and grid[x][y] == inf_val:
                    grid[x][y] = grid[i][j] + 1
                    q.append((x, y))

        return

        # 小提示：时间和空间复杂度都是 O(m·n)，每个格子最多入队一次，而且没有递归，不会爆栈
        # 小提示：不要对每个宝藏分别跑一次 BFS，那样是 O(k·m·n)。
        #   多源 BFS 一开始就把所有起点放进队列，只需要跑一遍

        m, n = len(grid), len(grid[0])

        def dfs(i, j, count):
            if 0 <= i < m and 0 <= j < n and grid[i][j] > 0:
                if grid[i][j] > count:
                    grid[i][j] = count
                    for a, b in [(1,0),(0,1),(-1,0),(0,-1)]:
                        dfs(i+a, j+b, count+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    for a, b in [(1,0),(0,1),(-1,0),(0,-1)]:
                        dfs(i+a, j+b, 1)

        return