class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        xorr = n

        for i in range(n):
            xorr ^= i ^ nums[i]
            
        return xorr

        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return len(nums)
        
        return (len(nums) * (len(nums)+1)) // 2 - sum(nums) 