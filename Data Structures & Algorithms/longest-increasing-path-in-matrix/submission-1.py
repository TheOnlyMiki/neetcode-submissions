class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])

        dp = {}
        
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i,j)]

            dp[(i,j)] = 1

            for a,b in [(1,0), (0,1), (-1,0), (0,-1)]:
                x,y = i+a, j+b

                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    dp[(i,j)] = max(dp[(i,j)], 1 + dfs(x,y))

            return dp[(i,j)]

        for i in range(m):
            for j in range(n):
                dfs(i, j)

        return max(dp.values())