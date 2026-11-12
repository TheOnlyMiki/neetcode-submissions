class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])

        fresh = 0

        level = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    level.append((i,j))

        output = 0

        while level and fresh > 0:
            next_level = []
            output += 1

            for i, j in level:
                for a,b in [(1,0),(0,1),(-1,0),(0,-1)]:
                    x,y = i+a,j+b

                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1

                        next_level.append((x,y))

            level = next_level

        return output if fresh == 0 else -1
