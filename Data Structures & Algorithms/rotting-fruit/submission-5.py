class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        题目：网格中 0 为空格，1 为新鲜橘子，2 为腐烂橘子。
             每分钟，腐烂橘子会让上下左右相邻的新鲜橘子腐烂。
             返回所有橘子都腐烂所需的最少分钟数；不可能全部腐烂则返回 -1。
        思路：多源 BFS（和"岛屿与宝藏 / 墙与门"同一个模型）
        - 所有初始腐烂的橘子同时作为起点放进第一层
        - 每一层代表一分钟：这一层的腐烂橘子把相邻的新鲜橘子变成下一层
        - 用 fresh 记录剩余新鲜橘子数，全部腐烂后就可以停止
        例：grid = [[2,1,1],
                    [1,1,0],
                    [0,1,1]]
            第 1 分钟：(0,1)(1,0) 腐烂
            第 2 分钟：(0,2)(1,1) 腐烂
            第 3 分钟：(2,1) 腐烂
            第 4 分钟：(2,2) 腐烂 → 返回 4
        时间复杂度 O(m · n)：每个格子最多入队一次
        空间复杂度 O(m · n)：最坏情况下一层存下大部分格子

        小提示：
        - 循环条件里的 fresh > 0 很重要：最后一批橘子腐烂后立刻停止，
          不会因为最后一层还要"空转"一轮而让分钟数多算 1。
          （常见错误写法是 while level，最后再 mins - 1，容易在边界情况出错）
        - 开头的 if fresh == 0: return 0 其实可以省略：
          fresh 为 0 时 while 不执行，mins 为 0，最后返回 0，结果一样。
        - 用 fresh 计数代替最后再扫一遍网格检查有没有剩下的 1，少一次 O(m · n) 遍历。
        - 把 grid[x][y] 改成 2 同时起到 visited 的作用，同一个橘子不会被重复入队。
        - 按层处理用的是 level / next_level 两个列表，也可以用 deque，
          每轮先记下 len(q)，只弹出这么多个，效果相同。
        - 同类多源 BFS：LeetCode 286（墙与门）、542（01 矩阵）、1162（地图分析）。
        """

        m, n = len(grid), len(grid[0])

        level = []   # 当前这一分钟的腐烂橘子（BFS 当前层）

        fresh = 0    # 剩余新鲜橘子数

        # ---------- 第 1 步：统计新鲜橘子，所有腐烂橘子作为起点 ----------
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    level.append((i,j))

        # 一开始就没有新鲜橘子，不需要时间
        if fresh == 0:
            return 0

        mins = 0   # 已经过去的分钟数

        # ---------- 第 2 步：逐层扩散，每层代表一分钟 ----------
        # 还有能传播的腐烂橘子，且还有新鲜橘子，才继续
        while level and fresh > 0:
            next_level = []
            mins += 1

            for i, j in level:
                for a, b in [(1,0),(0,1),(-1,0),(0,-1)]:
                    x, y = i+a, j+b

                    # 相邻的新鲜橘子在这一分钟腐烂
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2           # 标记腐烂，同时防止重复入队
                        next_level.append((x,y)) # 下一分钟由它继续传播
                        fresh -= 1

            level = next_level

        # 还有新鲜橘子没腐烂：被空格隔开，永远到不了
        return mins if fresh == 0 else -1