class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s3) != len(s1) + len(s2):
            return False

        length_1, length_2 = len(s1), len(s2)

        dp = [[False] * (length_2+1) for i in range(length_1+1)]
        dp[length_1][length_2] = True

        for i in range(length_1, -1, -1):
            for j in range(length_2, -1, -1):
                if i < length_1 and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < length_2 and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True

        return dp[0][0]
        
        if len(s3) != len(s1) + len(s2):
            return False

        length_1, length_2 = len(s1), len(s2)

        dp = {}

        def dfs(i, j):
            if i + j == len(s3):
                return i == length_1 and j == length_2

            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = False

            if i < length_1 and s1[i] == s3[i + j]:
                dp[(i, j)] = dfs(i+1, j)

            if not dp[(i, j)] and j < length_2 and s2[j] == s3[i + j]:
                dp[(i, j)] = dfs(i, j+1)

            return dp[(i, j)]
            
        return dfs(0, 0)

            