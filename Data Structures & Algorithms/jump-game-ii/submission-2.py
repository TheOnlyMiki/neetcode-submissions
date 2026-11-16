class Solution:
    def jump(self, nums: List[int]) -> int:
        
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
