class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m,n = len(heights), len(heights[0])

        output = []

        pacific = set()
        atlantic = set()
        
        def dfs(i, j, visit):
            visit.add((i, j))

            for a, b in [(1,0),(0,1),(-1,0),(0,-1)]:
                x,y = i+a,j+b
                if 0 <= x < m and 0 <= y < n and (x, y) not in visit and heights[x][y] >= heights[i][j]:
                    dfs(x, y, visit)

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n-1, atlantic)

        for j in range(n):
            dfs(0, j, pacific)
            dfs(m-1, j, atlantic)

        return list(pacific & atlantic)
            