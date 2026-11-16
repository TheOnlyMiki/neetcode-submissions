class Solution:
    def checkValidString(self, s: str) -> bool:

        stack_open = []
        stack_star = []

        for i, c in enumerate(s):
            if c == '(':
                stack_open.append(i)
            elif c == '*':
                stack_star.append(i)
            else:
                if not stack_open and not stack_star:
                    return False
                    
                if stack_open:
                    stack_open.pop()
                else:
                    stack_star.pop()

        while stack_open and stack_star:
            if stack_open.pop() > stack_star.pop():
                return False

        return len(stack_open) == 0

        dp = {}
        
        def dfs(i, diff):
            if diff < 0:
                return False
                
            if i == len(s):
                return diff == 0

            if (i, diff) in dp:
                return dp[(i, diff)]
            
            if s[i] == '(':
                dp[(i, diff)] = dfs(i+1, diff+1)
            elif s[i] == ')':
                dp[(i, diff)] = dfs(i+1, diff-1)
            else:
                dp[(i, diff)] = dfs(i+1, diff+1) or dfs(i+1, diff-1) or dfs(i+1, diff)

            return dp[(i, diff)]

        return dfs(0, 0)

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
            
            