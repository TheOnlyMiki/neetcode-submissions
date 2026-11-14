class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        sums = sum(nums)

        if sums % 2 == 1:
            return False

        target = sums // 2

        n = len(nums)

        record = [[-1] * (target + 1) for i in range(n)]

        def dfs(i, target):
            if target == 0:
                return True

            if i >= n or target < 0:
                return False

            if record[i][target] != -1:
                return record[i][target]

            record[i][target] = dfs(i+1, target) or dfs(i+1, target - nums[i])

            return record[i][target]

        return dfs(0, target)