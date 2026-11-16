class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s3) != len(s1) + len(s2):
            return False

        length_1, length_2 = len(s1), len(s2)

        dp = {}

        def dfs(i_1, i_2):
            if i_1 + i_2 == len(s3):
                return i_1 == length_1 and i_2 == length_2

            if (i_1, i_2) in dp:
                return dp[(i_1, i_2)]

            dp[(i_1, i_2)] = False

            if i_1 < length_1 and s1[i_1] == s3[i_1 + i_2]:
                dp[(i_1, i_2)] = dfs(i_1+1, i_2)

            if not dp[(i_1, i_2)] and i_2 < length_2 and s2[i_2] == s3[i_1 + i_2]:
                dp[(i_1, i_2)] = dfs(i_1, i_2+1)

            return dp[(i_1, i_2)]
            
        return dfs(0, 0)

            