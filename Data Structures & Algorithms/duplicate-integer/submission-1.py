class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''record = set(nums)
        return len(record) != len(nums)
        # time complexity O(n), space complexity O(n)'''

        # Method 2:
        record = set()
        for num in nums:
            if num in record:
                return True
            record.add(num)
        return False