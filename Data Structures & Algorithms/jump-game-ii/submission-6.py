class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        
        l, r = 0, 0

        step = 0

        while r < n-1:
            step += 1

            most_far = 0
            for i in range(l, r+1):
                if i + nums[i] > most_far:
                    most_far = i + nums[i]
                    
            l = r+1
            r = most_far

        return step
















































        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(n-1):
            end = min(n, i+nums[i]+1)
            for j in range(i+1, end):
                dp[j] = min(dp[j], dp[i]+1)

        return dp[n-1]

        step = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            most_far = 0
            for i in range(l, r + 1):
                most_far = max(most_far, i + nums[i])

            l = r + 1
            r = most_far

            step += 1

        return step
        
        most_far = 0
        step = 0
        i = 0

        while i < len(nums)-1:
            step += 1

            if i + nums[i] >= len(nums)-1:
                break

            most_far = max(most_far, i + nums[i])

            i_most_far = i+1
            for j in range(i+1, most_far+1):
                if j + nums[j] > i_most_far + nums[i_most_far]:
                    i_most_far = j

            i = i_most_far

        return step
