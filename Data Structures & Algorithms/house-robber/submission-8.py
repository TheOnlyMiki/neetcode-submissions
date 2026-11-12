class Solution:
    def rob(self, nums: List[int]) -> int:

        # DP space O(1)

        if len(nums) < 2:
            return nums[0]

        n = len(nums)

        pre_house_2, pre_house_1 = 0, 0 
        output = 0

        for i in range(n):
            output = max(pre_house_1, pre_house_2 + nums[i])

            pre_house_2, pre_house_1 = pre_house_1, output

        return output

        # DP

        if len(nums) < 2:
            return nums[0]

        n = len(nums)
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[n-1]
