class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

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
