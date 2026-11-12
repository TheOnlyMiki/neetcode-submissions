class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Method 2 - 寻找一条完美的“中线”，把数据切成两半
        # 中位数的本质是将一个集合划分为两个长度相等的部分，且左半部分的所有元素都小于或等于右半部分的所有元素。
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        median_length = (m + n + 1) // 2

        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = median_length - i

            nums1_left_max = nums1[i-1] if i > 0 else -float('inf')
            nums1_right_min = nums1[i] if i < m else float('inf')

            nums2_left_max = nums2[j-1] if j > 0 else -float('inf')
            nums2_right_min = nums2[j] if j < n else float('inf')

            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                if (m + n) % 2 == 1:
                    return max(nums1_left_max, nums2_left_max)
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0

            if nums1_left_max > nums2_right_min:
                right = i - 1
            else:
                left = i + 1

        return 0.0

        # Method 1 - 先排序再找（双指针双路归并模拟法）
        m, n = len(nums1), len(nums2)
        length = m + n
        
        # i, j 分别作为 nums1 和 nums2 的遍历指针
        i, j = 0, 0
        
        # val 记录当前遍历到的值，pre_val 记录上一次遍历到的值（用于偶数长度时求平均数）
        val = None
        pre_val = None
        
        # 中位数最多只需要知道合并后前 length // 2 + 1 个元素即可
        for _ in range(length // 2 + 1):
            # 在更新 val 之前，先将当前值存入 pre_val
            pre_val = val
            
            # 情况 1：nums1 已经全部遍历完，只能从 nums2 中取值
            if i == m:
                val = nums2[j]
                j += 1
            # 情况 2：nums2 已经全部遍历完，只能从 nums1 中取值
            elif j == n:
                val = nums1[i]
                i += 1
            # 情况 3：两个数组都未遍历完，取 nums1 当前较小的值
            elif nums1[i] < nums2[j]:
                val = nums1[i]
                i += 1
            # 情况 4：两个数组都未遍历完，取 nums2 当前较小（或相等）的值
            else:
                val = nums2[j]
                j += 1
                
        # 如果总长度是偶数，中位数是中间两个数的平均值
        if length % 2 == 0:
            val = (pre_val + val) / 2
            
        # 如果总长度是奇数，直接返回 val 即可
        return val
        # 时间复杂度: O(m + n)
        # 空间复杂度: O(1)
