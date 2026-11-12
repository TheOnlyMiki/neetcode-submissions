class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # Method 1 - 先排序再找
        m, n = len(nums1), len(nums2)
        length = m + n
        
        median = length // 2

        i, j = 0, 0
        val = None
        pre_val = None

        for _ in range(median+1):
            if i == m:
                pre_val = val
                val = nums2[j]
                j += 1
                continue
            elif j == n:
                pre_val = val
                val = nums1[i]
                i += 1
                continue
            
            if nums1[i] < nums2[j]:
                pre_val = val
                val = nums1[i]
                i += 1
            else:
                pre_val = val
                val = nums2[j]
                j += 1

        if length % 2 == 0:
            val = (pre_val + val) / 2
        
        return val