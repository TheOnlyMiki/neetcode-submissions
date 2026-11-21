class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        if len(t) >= len(s):
            return 1 if t == s else 0

        dp = {}

        def dfs(i, j):
            if (i,j) in dp:
                return dp[(i,j)]

            if j == len(t):
                return 1

            if i == len(s):
                return 0

            count = dfs(i+1, j)

            if s[i] == t[j]:
                count += dfs(i+1, j+1)

            dp[(i,j)] = count

            return count

        return dfs(0, 0)