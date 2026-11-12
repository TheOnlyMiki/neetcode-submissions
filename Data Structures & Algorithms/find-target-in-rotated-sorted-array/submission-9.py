class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Method 2 - 先找到最小值 index 然后在决定去哪边找

        # 1. 通过二分查找，先找到整个旋转数组中的“最小值索引”（即旋转点）
        '''left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # 如果中点值大于右端点值，说明最小值一定在 mid 的右侧
            if nums[mid] > nums[right]:
                left = mid + 1
            # 否则，最小值在 mid 左侧或者就是 mid 本身
            else:
                right = mid

        # 此时 left 和 right 重合，i 就是最小值的索引（旋转点的断层位置）
        i = left
        
        # 阶段二：利用最小值索引 i，判断 target 落在左边还是右边的单调递增区间
        left, right = 0, len(nums) - 1
        
        # 如果 target 大于等于最小值，且小于等于最右端的值，说明 target 落在右半边有序区间
        if target >= nums[i] and target <= nums[right]:
            left = i        # 将左边界锁定在右半边 [i, len(nums)-1]
        # 否则，target 必定落在左半边有序区间
        else:
            right = i - 1   # 将右边界锁定在左半边 [0, i-1]

        # 阶段三：在锁定后的标准单调递增区间内，进行常规的二分查找
        while left <= right:
            mid = (left + right) // 2
            
            # 目标值在右侧，向右收缩
            if nums[mid] < target:
                left = mid + 1
            # 目标值在左侧，向左收缩
            elif nums[mid] > target:
                right = mid - 1
            # 找到目标值，直接返回其对应的数组下标
            else:
                return mid

        # 如果二分结束仍未找到，说明 target 不在数组中
        return -1

        # 时间复杂度 O(log N)
        # 其中 N 是 nums 数组的长度。
        # 算法由两个独立的二分查找组成：第一个二分用 log N 时间找到最小值索引，第二个二分用 log N 时间在目标半区查找 target。
        # O(log N) + O(log N) 依然是 O(log N)。
        #
        # 空间复杂度 O(1)
        # 算法仅使用了常数级别的额外变量空间（left, right, mid, i 等），没有借用任何额外的数据结构。

'''
        # Method 1 - 直接在里面查找
        
        # 初始化左右双指针，定义搜索区间的边界
        left, right = 0, len(nums) - 1

        # 使用标准的二分查找循环，闭区间 [left, right]
        while left <= right:
            # 计算中间位置索引，向下取整
            mid = (left + right) // 2

            # 如果中间元素正是目标值，直接返回对应的索引
            if nums[mid] == target:
                return mid

            # 情况 1：左半部分是有序的（例如：[4, 5, 6, 7, 0, 1, 2]，mid 落在左侧递增段）
            if nums[left] <= nums[mid]:
                # 核心分类讨论：判断 target 是否【不在】这个有序的左半部分
                # 1. target > nums[mid]: 说明 target 比左半部分的最大值还要大
                # 2. target < nums[left]: 说明 target 比左半部分的最小值还要小
                # 满足任一条件，都意味着 target 必然在右半部分，因此收缩左边界
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                # 否则，target 必定在有序的左半部分 [left, mid - 1] 之间，收缩右边界
                else:
                    right = mid - 1

            # 情况 2：右半部分是有序的（例如：[6, 7, 0, 1, 2, 4, 5]，mid 落在右侧递增段）
            else:
                # 核心分类讨论：判断 target 是否【不在】这个有序的右半部分
                # 1. target < nums[mid]: 说明 target 比右半部分的最小值还要小
                # 2. target > nums[right]: 说明 target 比右半部分的最大值还要大
                # 满足任一条件，都意味着 target 必然在左半部分，因此收缩右边界
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                # 否则，target 必定在有序的右半部分 [mid + 1, right] 之间，收缩左边界
                else:
                    left = mid + 1

        # 如果循环结束仍未找到目标值，说明 target 不在数组中，返回 -1
        return -1
        #时间复杂度: O(log n))。每一次循环通过条件判断，都能稳定排除掉一半的搜索区间，完全契合二分查找的核心效率。
        # 空间复杂度: (O(1))。仅使用了 left, right, mid 几个常数级别的变量指针，没有消耗额外的内存空间。

