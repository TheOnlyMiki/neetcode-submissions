class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = {}

        def dfs(i, j):
            if i == m-1 and j == n-1:
                return 1
            if i >= m or j >= n:
                return 0

            if (i, j) in dp:
                return dp[(i,j)]

            dp[(i,j)] = dfs(i+1,j) + dfs(i, j+1)

            return dp[(i,j)]

        return dfs(0, 0)


        dp = {}

        def dfs(i, j):
            if i == m-1 and j == n-1:
                return 1

            if i >= m or j >= n:
                return 0

            if (i, j) in dp:
                return dp[(i,j)]

            dp[(i,j)] = dfs(i+1, j) + dfs(i, j+1)

            return dp[(i,j)]

        return dfs(0, 0)

        dp = {}

        def dfs(i, j):
            if i == 0 and j == 0:
                return 1

            if i < 0 or j < 0:
                return 0

            if (i, j) in dp:
                return dp[(i,j)]

            dp[(i,j)] = dfs(i-1, j) + dfs(i, j-1)

            return dp[(i, j)]

        return dfs(m-1, n-1)

        
        dp = [[0] * (n+1) for i in range(m+1)]
        dp[0][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m][n]