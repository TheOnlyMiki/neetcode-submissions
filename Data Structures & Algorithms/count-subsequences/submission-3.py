class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
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