class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)

        output = 0

        for num in nums:
            if num - 1 in nums:
                continue

            count = 1

            while num + count in nums:
                count += 1

            output = max(output, count)

        return output
