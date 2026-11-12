class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Method 1 - 哈希表

        record = set()

        for num in nums:
            if num in record:
                return num
            record.add(num)