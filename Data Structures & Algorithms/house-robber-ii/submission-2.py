class Solution:
    def rob(self, nums: List[int]) -> int:

        # DP space O(1)

        if len(nums) < 4:
            return max(nums)

        n = len(nums)

        pre_house_2, pre_house_1 = 0, 0
        rob1 = 0

        for i in range(n-1):
            rob1 = max(pre_house_1, pre_house_2 + nums[i])
            pre_house_2, pre_house_1 = pre_house_1, rob1

        pre_house_2, pre_house_1 = 0, 0
        rob2 = 0

        for i in range(1, n):
            rob2 = max(pre_house_1, pre_house_2 + nums[i])
            pre_house_2, pre_house_1 = pre_house_1, rob2

        return max(rob1, rob2)

        # DP
        
        if len(nums) < 4:
            return max(nums)

        n = len(nums)

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, n-1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        rob1 = dp[n-2]

        dp = [0] * n
        dp[1] = nums[1]
        dp[2] = max(dp[1], nums[2])

        for i in range(3, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return max(rob1, dp[n-1])