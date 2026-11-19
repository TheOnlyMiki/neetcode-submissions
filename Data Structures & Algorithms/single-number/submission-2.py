class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        seen = set()

        for num in nums:

            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
                
        return list(seen)[0]

        nums.sort()
        i = 0

        while i < len(nums) - 1:

            if nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]

        return nums[i]
        
        temp = 0

        for num in nums:
            temp = temp ^ num

        return temp