class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] != 0:
                size = grid[i][j]

                grid[i][j] = 0

                for a, b in [(1,0),(0,1),(-1,0),(0,-1)]:
                    size += dfs(i+a, j+b)

                return size

            return 0

        best = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    best = max(best, dfs(i, j))

        return best