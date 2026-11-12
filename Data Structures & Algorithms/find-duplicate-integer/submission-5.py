class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Method 3 - 修改数组为负数

        for num in nums:
            i = abs(num) - 1
            if nums[i] < 0:
                return abs(num)
            
            nums[i] *= -1

        return -1

        # Method 2 - 排序后，只需要对比是否相等，但是会修改数组或者排序不一定是空间为O(1)

        nums = sorted(nums)

        pre_num = nums[0]-1

        for num in nums:
            if num == pre_num:
                return num
            pre_num = num

        return

        # Method 1 - 哈希表,空间 O(n)

        record = set()

        for num in nums:
            if num in record:
                return num
            record.add(num)

        return
