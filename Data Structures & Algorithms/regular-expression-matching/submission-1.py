class Solution:
    def isMatch(self, s: str, p: str) -> bool:

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
