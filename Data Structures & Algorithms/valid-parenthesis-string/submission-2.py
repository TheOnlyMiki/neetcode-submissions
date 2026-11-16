class Solution:
    def checkValidString(self, s: str) -> bool:

        dp = {}
        
        def dfs(i, left, right):
            if right > left:
                return False
                
            if i == len(s):
                return left == right

            if (i, left, right) in dp:
                return dp[(i, left, right)]

            dp[(i, left, right)] = False
            
            if s[i] == '(':
                dp[(i, left, right)] = dfs(i+1, left+1, right)
            elif s[i] == ')':
                dp[(i, left, right)] = dfs(i+1, left, right+1)
            else:
                dp[(i, left, right)] = dfs(i+1, left+1, right) or dfs(i+1, left, right+1) or dfs(i+1, left, right)

            return dp[(i, left, right)]

        return dfs(0, 0, 0)
            
            