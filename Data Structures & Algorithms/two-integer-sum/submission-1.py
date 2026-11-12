class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if len(nums) < 2:
            return False
        '''
        pair = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in pair:
                return [pair[diff], i]
            pair[nums[i]] = i

        return False
        '''

        remain = {}
        for i, num in enumerate(nums):
            if target - num in remain:
                remain = [remain[target - num], i]
                break
            remain[num] = i

        return remain
        # time complexity O(n), space complexity O(n)