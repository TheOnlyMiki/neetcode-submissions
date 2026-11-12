class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 1, 1
        output = [1] * n

        # left
        for i in range(n):
            output[i] = output[i] * left
            left = left * nums[i]

        # right
        for i in range(n-1, -1, -1):
            output[i] = output[i] * right
            right = right * nums[i]

        return output