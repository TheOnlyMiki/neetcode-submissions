class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # Method 1 - 先排序再找
        m, n = len(nums1), len(nums2)
        length = m + n

        i, j = 0, 0
        val = None
        pre_val = None

        for _ in range(length // 2 + 1):
            pre_val = val

            if i == m:
                val = nums2[j]
                j += 1
            elif j == n:
                val = nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                val = nums1[i]
                i += 1
            else:
                val = nums2[j]
                j += 1

        if length % 2 == 0:
            val = (pre_val + val) / 2
        
        return val