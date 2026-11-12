class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m, n = len(heights), len(heights[0])

        def dfs(i, j, visit):
            visit.add((i, j))

            for a, b in [(1,0),(0,1),(-1,0),(0,-1)]:
                x, y = i+a, j+b
                if 0 <= x < m and 0 <= y < n and (x,y) not in visit and heights[x][y] >= heights[i][j]:
                    dfs(x, y, visit)

        pacific = set()
        atlantic = set()

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n-1, atlantic)

        for i in range(n):
            dfs(0, i, pacific)
            dfs(m-1, i, atlantic)

        return [[i,j] for i,j in (pacific & atlantic)]