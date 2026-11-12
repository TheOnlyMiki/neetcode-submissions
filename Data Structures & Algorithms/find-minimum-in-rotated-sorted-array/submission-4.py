from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums)-1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]






































        # 1. 初始化二分查找的左右指针（指针代表数组的索引下标）
        left, right = 0, len(nums) - 1

        # 2. 开始二分查找，当 left == right 时说明收敛到唯一元素，退出循环
        while left < right:
            mid = (left + right) // 2
            cur = nums[mid]

            # 3. 核心优化：如果当前区间左端点严格小于右端点
            # 说明当前 [left, right] 区间是绝对单调递增的（没有被旋转截断）
            # 那么最左边的元素 nums[left] 必然是该区间的最小值，直接返回
            if nums[left] < nums[right]:
                return nums[left]
                
            # 4. 如果中点值大于右端点值
            # 说明中点 mid 仍落在左边那个“较大的”递增段里
            # 那么旋转点（最小值）一定在 mid 的严格右侧，所以跳过 mid
            elif cur > nums[right]:
                left = mid + 1
                
            # 5. 如果中点值小于或等于右端点值
            # 说明中点 mid 已经落在了右边那个“较小的”递增段里（或者当前区间本身就有序）
            # 此时最小值可能是 mid 本身，也可能在 mid 的左侧，所以 right 缩小到 mid
            else:
                right = mid

        # 6. 当指针重合时，left 指向的就是旋转数组中的最小元素
        return nums[left]

        # 时间复杂度 O(log N)
        # 其中 N 是 nums 数组的长度。每次循环都通过 mid 将搜索区间减半，因此是典型的对数级时间。
        # 空间复杂度 O(1)
        # 算法只使用了常数级别的额外空间（left, right, mid, cur 变量）。
