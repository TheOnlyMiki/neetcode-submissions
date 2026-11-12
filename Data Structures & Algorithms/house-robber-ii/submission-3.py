class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        题目：打家劫舍 II。房屋围成一圈（第一间和最后一间相邻），不能偷相邻的两间，求最大金额。
        思路：把环拆成两条直线，复用 LeetCode 198（打家劫舍）
        - 环带来的唯一新限制：第一间和最后一间不能同时偷
        - 所以最优解一定属于以下两种情况之一：
          · 不偷最后一间 → 在 nums[0 : n-1] 上做普通打家劫舍，得到 rob1
          · 不偷第一间   → 在 nums[1 : n]   上做普通打家劫舍，得到 rob2
        - 答案 = max(rob1, rob2)
        （两种情况有重叠，比如首尾都不偷的方案两边都包含，但取最大值不受影响）
        例：nums = [2, 3, 2]
            不偷最后一间：[2, 3] → 3
            不偷第一间  ：[3, 2] → 3
            答案 3（不能偷 2 + 2，因为首尾相邻）
        时间复杂度 O(n)：两次线性 DP
        空间复杂度：Method 2 为 O(1)，Method 1 为 O(n)

        小提示：
        - 少于 4 间房时，任意两间都相邻（环上 3 间两两相邻），只能偷一间，所以返回 max(nums)。
          对 Method 2 来说其实只需要特判 n == 1：
          n = 1 时两个循环的范围都是空的，rob1、rob2 都为 0，会返回错误的 0；
          n = 2、3 时滚动变量的写法会自然得到正确答案。
          Method 1 则需要保留 n < 4 的特判，否则 dp[2]、dp[n-2] 等下标会越界或取错。
        - 两段循环代码几乎一样，可以抽成辅助函数，代码更短也更不容易写错：
              def rob_line(houses):
                  pre2, pre1 = 0, 0
                  for money in houses:
                      pre2, pre1 = pre1, max(pre1, pre2 + money)
                  return pre1
              if len(nums) == 1:
                  return nums[0]
              return max(rob_line(nums[:-1]), rob_line(nums[1:]))
          切片会复制数组，额外 O(n) 空间；在意的话可以传起止下标。
        - "环形拆成两段线性"是处理环形 DP 的常用技巧，
          类似还有 LeetCode 918（环形子数组的最大和：最大值要么在中间，要么跨越首尾 = 总和 - 中间最小子数组）。
        """

        # ==================== Method 2 - 动态规划，滚动变量，空间 O(1) ====================

        # 少于 4 间房：所有房屋两两相邻，只能偷一间
        if len(nums) < 4:
            return max(nums)

        n = len(nums)

        # ---------- 情况 1：不偷最后一间，考虑下标 0 ~ n-2 ----------
        # pre_house_2：dp[i-2]，pre_house_1：dp[i-1]，初始为 0 相当于前面补两间空房
        pre_house_2, pre_house_1 = 0, 0
        rob1 = 0

        for i in range(n-1):
            # 不偷第 i 间：pre_house_1；偷第 i 间：pre_house_2 + nums[i]
            rob1 = max(pre_house_1, pre_house_2 + nums[i])
            pre_house_2, pre_house_1 = pre_house_1, rob1

        # ---------- 情况 2：不偷第一间，考虑下标 1 ~ n-1 ----------
        pre_house_2, pre_house_1 = 0, 0
        rob2 = 0

        for i in range(1, n):
            rob2 = max(pre_house_1, pre_house_2 + nums[i])
            pre_house_2, pre_house_1 = pre_house_1, rob2

        # 两种情况取较大值
        return max(rob1, rob2)

        # ==================== Method 1 - 动态规划，dp 数组 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留

        # 少于 4 间房：只能偷一间（同时避免下面的下标越界）
        if len(nums) < 4:
            return max(nums)

        n = len(nums)

        # ---------- 情况 1：不偷最后一间，dp 只算到下标 n-2 ----------
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, n-1):
            # 不偷第 i 间沿用 dp[i-1]，偷第 i 间加上 dp[i-2]
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        rob1 = dp[n-2]

        # ---------- 情况 2：不偷第一间，dp 从下标 1 开始算 ----------
        # dp[0] 保持为 0，表示第一间不偷
        dp = [0] * n
        dp[1] = nums[1]
        dp[2] = max(dp[1], nums[2])

        for i in range(3, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        # 两种情况取较大值
        return max(rob1, dp[n-1])