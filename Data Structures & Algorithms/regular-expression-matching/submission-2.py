class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        length_s, length_p = len(s), len(p)

        dp = [[False] * (length_p+1) for _ in range(length_s+1)]

        dp[length_s][length_p] = True

        for i in range(length_s, -1, -1):
            for j in range(length_p-1, -1, -1):
                match = i < length_s and (p[j] == s[i] or p[j] == '.')

                if j+1 < length_p and p[j+1] == '*':
                    dp[i][j] = (dp[i][j+2] or (match and dp[i+1][j]))
                else:
                    dp[i][j] = (match and dp[i+1][j+1])

        return dp[0][0]

        length_s, length_p = len(s), len(p)
        
        dp = {}

        def dfs(i, j):
            if j == length_p:
                return i == length_s

            if (i,j) in dp:
                return dp[(i,j)]

            match = False

            if i < length_s and (p[j] == s[i] or p[j] == '.'):
                match = True

            if j+1 < length_p and p[j+1] == '*':
                dp[(i, j)] = dfs(i, j+2) or (match and dfs(i+1, j))
            else:
                dp[(i, j)] = match and dfs(i+1, j+1)

            return dp[(i,j)]

        return dfs(0, 0)
