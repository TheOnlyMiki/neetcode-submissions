class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        record = set(nums)
        best = 0

        for i in range(len(nums)):
            if nums[i]-1 in record:
                continue

            output = 1
            temp = nums[i]+1
            while temp in record:
                temp += 1
                output += 1

            if output > best:
                best = output

        return best

        # Method 1 - sort
        '''if not nums:
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
        
        return best'''
        # time complexity O(nlogn + n), space complexity O(n) or O(1)

        # Method 2
        record = set(nums)

        best = 0
        for num in nums:
            if num-1 not in record:
                length = 1
                while num+length in record:
                    length += 1
                if length > best:
                    best = length

        return best
        # time comlexity O(n), space complexity O(n)
