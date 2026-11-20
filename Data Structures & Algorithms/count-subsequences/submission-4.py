class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        length_s, length_t = len(s), len(t)

        dp = [[0] * (length_t+1) for _ in range(length_s+1)]

        for i in range(length_s+1):
            dp[i][length_t] = 1

        for i in range(length_s-1, -1, -1):
            for j in range(length_t-1, -1, -1):
                dp[i][j] += dp[i+1][j]

                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]

        return dp[0][0]
        
        dp = {}

        def dfs(i, j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0

            if (i,j) in dp:
                return dp[(i,j)]

            count = dfs(i+1, j)

            if s[i] == t[j]:
                count += dfs(i+1, j+1)

            dp[(i,j)] = count

            return dp[(i,j)]

        return dfs(0, 0)