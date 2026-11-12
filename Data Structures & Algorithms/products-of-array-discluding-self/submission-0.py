class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Method 1 - devide
        zero_count = []
        product = 1
        for i, n in enumerate(nums):
            if n == 0:
                zero_count.append(i)
            else:
                product *= n

        output = [0] * len(nums)

        if len(zero_count) != 0:
            if len(zero_count) == 1:
                output[zero_count[0]] = product
                
            return output

        for i, n in enumerate(nums):
            output[i] = int(product / nums[i])

        return output