class Solution:
    def countBits(self, n: int) -> List[int]:

        output = [0] * (n + 1)

        for i in range(1, n + 1):
            num = i

            while num != 0:
                remain_one = num & 1

                output[i] += remain_one

                num = num >> 1
                
        return output

        dp = [0] * (n + 1)

        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i

            dp[i] = 1 + dp[i - offset]

        return dp

        if n == 0:
            return [0]
        
        dp = [0] * (n+1)

        dp[1] = 1

        for i in range(1, n+1):
            num = i >> 1

            dp[i] = dp[num] + (i & 1)

        return dp

