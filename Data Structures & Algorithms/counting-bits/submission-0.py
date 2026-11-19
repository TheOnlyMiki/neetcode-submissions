class Solution:
    def countBits(self, n: int) -> List[int]:

        if n == 0:
            return [0]
        
        dp = [0] * (n+1)

        dp[1] = 1

        for i in range(1, n+1):
            num = i >> 1

            dp[i] = dp[num] + (i & 1)

        return dp

