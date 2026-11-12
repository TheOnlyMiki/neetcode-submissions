class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Method 1 - devide
        """
        '''zero_count = []
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
            output[i] = int(product / nums[i])'''

        zero_count = 0
        product = 1
        for i, n in enumerate(nums):
            if n == 0:
                zero_count += 1
                if zero_count > 1:
                    return len(nums) * [0]
                continue
                
            product *= n

        output = []
        for n in nums:
            if zero_count == 1:
                output.append(int(product) if n == 0 else 0)
            else:
                output.append(int(product/n))

        return output"""
        # time complexity O(n), space complexity O(1), O(n) for output

        # Method 2 - left and right index
        n = len(nums)
        '''
        left = [1] * n
        right = [1] * n

        #Left
        initial = 1
        for i in range(1, n):
            left[i] = initial * nums[i-1]
            initial = left[i]
        #print(left)

        #Right
        initial = 1
        for i in range(1, n):
            right[i] = initial * nums[-i]
            initial = right[i]
        #print(right)

        output = [0] * n
        for i in range(n):
            output[i] = left[i] * right[-i-1]
        '''
        left = 1
        right = 1

        output = [1] * n

        #left
        for i in range(n):
            output[i] = output[i] * left
            left = left * nums[i]

        #right
        for i in range(n-1, -1, -1):
            output[i] = output[i] * right
            right = right * nums[i]

        return output
