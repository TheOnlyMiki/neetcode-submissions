class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        题目：返回数组中第 k 大的元素（按排序后的位置算，重复元素也各占一位）。
             要求不排序，尽量做到 O(n)。
        思路：快速选择（Quickselect），和 LeetCode 973（最接近原点的 K 个点）同一个模板，
             只是这里要找"第 k 大"，所以分区时把"更大的"放左边，按降序分区：
                 [ 比 pivot 大的 ]  pivot  [ 不比 pivot 大的 ]
                                     ↑
                                   下标 p
             降序排好后第 k 大就在下标 k - 1，所以目标是让 pivot 落在 k - 1：
             - p == k - 1：pivot 就是第 k 大 → 返回
             - p >  k - 1：左边比它大的已经超过 k - 1 个，答案在左半边
             - p <  k - 1：左边还不够，答案在右半边
        时间复杂度：平均 O(n)，最坏 O(n²)
        空间复杂度：递归栈平均 O(log n)，最坏 O(n)

        小提示：
        - 固定选末尾作为 pivot 有两种退化情况，LeetCode 215 的测试用例两种都有，可能超时：
          · 数组已经有序：每次 pivot 都是最大或最小值，每轮只排除一个元素
          · 大量重复元素（如全是 1）：Lomuto 分区里等于 pivot 的元素全被分到右边，
            即使随机选 pivot 也每次只能排除一个
          解决办法：随机选 pivot + 三路分区（> pivot、== pivot、< pivot），
          只要目标下标落在"等于 pivot"那一段，就直接返回，重复元素一次性全部解决：
              l, r, target = 0, len(nums) - 1, k - 1
              while True:
                  pivot = nums[random.randint(l, r)]
                  lt, i, gt = l, l, r
                  # 不变量：[l, lt-1] > pivot，[lt, i-1] == pivot，[gt+1, r] < pivot
                  while i <= gt:
                      if nums[i] > pivot:
                          nums[lt], nums[i] = nums[i], nums[lt]
                          lt += 1
                          i += 1
                      elif nums[i] < pivot:
                          # 换过来的 nums[gt] 还没检查过，所以 i 不动
                          nums[i], nums[gt] = nums[gt], nums[i]
                          gt -= 1
                      else:
                          i += 1
                  if target < lt:        # 答案在"更大"的那段
                      r = lt - 1
                  elif target > gt:      # 答案在"更小"的那段
                      l = gt + 1
                  else:                  # 落在"等于 pivot"的那段
                      return pivot
          这样写是迭代的，也顺便解决了递归深度可能超过 Python 上限的问题。
        - 堆解法更稳妥，最坏也是 O(n log k)：维护大小为 k 的最小堆，最后堆顶就是第 k 大
          （和 LeetCode 703 一模一样），或者直接用 heapq.nlargest(k, nums)[-1]。
        - 面试时可以先说堆解法保底，再说快速选择平均 O(n)，并主动提到随机 pivot 和三路分区。
        """

        def quickSelect(l, r):
            """
            在 nums[l..r] 中按降序分区并递归，直到 pivot 落在下标 k-1 处，返回该值。
            不变量：目标下标 k-1 始终在 [l, r] 区间内。
            """
            # 选区间末尾作为 pivot
            pivot_val = nums[r]

            # store：下一个"比 pivot 大的数"应该放的位置
            # 循环中始终保持 nums[l..store-1] 都比 pivot 大
            store = l
            for i in range(l, r):
                # 注意是 >：大的放左边，实现降序分区
                if nums[i] > pivot_val:
                    nums[i], nums[store] = nums[store], nums[i]
                    store += 1

            # 把 pivot 从末尾换到 store，它左边全是更大的数
            nums[store], nums[r] = nums[r], nums[store]

            # 根据 pivot 的最终位置，决定往哪一边继续
            if store > k - 1:
                # 比 pivot 大的数已经超过 k - 1 个，第 k 大在左半边
                return quickSelect(l, store - 1)
            elif store < k - 1:
                # 比 pivot 大的数还不够，第 k 大在右半边
                return quickSelect(store + 1, r)
            else:
                # pivot 恰好排在降序第 k 位
                return nums[store]

        return quickSelect(0, len(nums)-1)