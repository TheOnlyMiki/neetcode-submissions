class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        sums = sum(nums)

        if sums % 2 == 1:
            return False

        target = sums//2

        dp = [[-1] * (target+1) for i in range(len(nums))]

        def dfs(i, target):
            if target == 0:
                return True

            if i >= len(nums) or target < 0:
                return False

            if dp[i][target] != -1:
                return dp[i][target]

            dp[i][target] = dfs(i+1, target) or dfs(i+1, target - nums[i])

            return dp[i][target]

        return dfs(0, target)
