class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        m,n = len(grid), len(grid[0])
        
        level = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    level.append((i, j))

        while level:
            next_level = []

            for i, j in level:
                for a, b in [(1,0),(0,1),(-1,0),(0,-1)]:
                    x, y = i+a, j+b

                    if 0 <= x < m and 0 <= y < n and grid[x][y] > grid[i][j] + 1:
                        grid[x][y] = grid[i][j] + 1
                        next_level.append((x,y))

            level = next_level

        return
        