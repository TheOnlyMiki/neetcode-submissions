class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        def dfs(i, j):
            if i + j == len(s3):
                return True if i == len(s1) and j == len(s2) else False

            if (i,j) in dp:
                return dp[(i,j)]

            dp[(i,j)] = False

            if i < len(s1) and s1[i] == s3[i+j]:
                dp[(i,j)] = dfs(i+1, j)
            if not dp[(i,j)] and j < len(s2) and s2[j] == s3[i+j]:
                dp[(i,j)] = dfs(i, j+1)

            return dp[(i,j)]

        return dfs(0, 0)
