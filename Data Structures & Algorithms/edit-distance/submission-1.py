class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m, n = len(word1), len(word2)

        dp = [[0] * (n+1) for i in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i

        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],    # Delete
                        dp[i][j-1],    # Insert
                        dp[i-1][j-1]   # Replace
                    )

        return dp[m][n]

        length_word1 = len(word1)
        length_word2 = len(word2)
        
        dp = {}

        def dfs(i, j):
            if i == length_word1:
                return length_word2 - j
            
            if j == length_word2:
                return length_word1 - i

            if (i,j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i+1, j+1)
            else:
                dp[(i,j)] = 1 + min(
                    dfs(i+1, j),
                    dfs(i, j+1),
                    dfs(i+1, j+1)
                )

            return dp[(i,j)]

        return dfs(0, 0)
