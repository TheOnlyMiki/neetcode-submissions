class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Method 1 - sort
        if not nums:
            return 0

        nums = sorted(set(nums))
        
        temp = nums[0]
        cur = 1
        best = 1

        for num in nums:
            if num == temp + 1:
                cur += 1
            else:
                cur = 1

            if cur > best:
                best = cur
            
            temp = num
        
        return best

        '''
        i = 0
        record = set(nums[0])
        for num in nums:
            if num-1 in record or num+1 in record:
                i = 1'''