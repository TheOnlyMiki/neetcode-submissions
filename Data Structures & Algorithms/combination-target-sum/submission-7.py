class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        output = []

        def backtrack(start, path, sums):
            if sums == target:
                output.append(path[:])
                return

            for i in range(start, len(nums)):
                if sums + nums[i] > target:
                    continue

                path.append(nums[i])
                backtrack(i, path, sums + nums[i])
                path.pop()


        backtrack(0, [], 0)

        return output

















        """
        题目：给定互不相同的正整数数组 nums 和目标值 target，
             找出所有和为 target 的组合，同一个数可以无限次重复选取，
             组合不能重复（[2,2,3] 和 [2,3,2] 算同一个）。
        思路：回溯，和 LeetCode 78（子集）同一个框架，区别有三点：
        1. 下一层从 i 开始而不是 i + 1 → 允许重复选同一个数
        2. 但仍然不回头选更小下标的数 → 保证组合内下标非递减，避免重复组合
        3. 只在和恰好等于 target 时记录结果；和超过 target 就剪枝
        例：nums = [2, 3, 6, 7]，target = 7
            [2,2,3]：2 → 2 → 3（下一层从当前下标开始，所以能连续选 2）
            [7]
            不会出现 [2,3,2]，因为选了 3 之后下一层只能从 3 开始
        时间复杂度：指数级，约 O(n^(T/M))，T 为 target，M 为 nums 中最小值（递归树最大深度 T/M）
        空间复杂度 O(T/M)：递归深度和 path 长度（不算输出）

        小提示：
        - 剪枝优化：先对 nums 排序，把 continue 改成 break。
          排序后 nums[i] 递增，一旦 sums + nums[i] > target，后面的数只会更大，
          整个循环都可以直接结束，比逐个 continue 少很多无效判断：
              nums.sort()
              ...
              if sums + nums[i] > target:
                  break
        - 也可以不传 sums，而是传"剩余值" remain = target - sums，减到 0 时记录，写法等价。
        - 因为 nums 全是正数，和只会越加越大，超过 target 后不可能再回到 target，剪枝才成立；
          如果有负数或 0，这个剪枝就不对了（题目保证都是正数）。
        - 同系列题对比（下一层的起点是关键）：
          · LeetCode 39（本题）：可重复选，backtrack(i, ...)
          · LeetCode 40（组合总和 II）：每个数只能用一次且 nums 有重复，
            backtrack(i + 1, ...)，排序后同层跳过重复：if i > start and nums[i] == nums[i-1]: continue
          · LeetCode 216（组合总和 III）：从 1~9 选 k 个数，额外限制 path 长度
        """

        output = []   # 所有满足条件的组合

        def backtrack(start, path, sums):
            """
            start：本层可以从 nums[start:] 中选数（允许继续选 nums[start] 本身）
            path ：当前已选的数
            sums ：当前已选数的和
            """
            # 和恰好等于目标：找到一个组合，记录（必须复制）并返回
            # 由于全是正数，再往下选只会更大，不需要继续递归
            if sums == target:
                output.append(path[:])
                return

            for i in range(start, len(nums)):
                # 剪枝：加上 nums[i] 就超过目标，这个数不能选
                # （未排序时后面的数可能更小，所以只能 continue 跳过当前数）
                if sums + nums[i] > target:
                    continue

                path.append(nums[i])                 # 做选择
                backtrack(i, path, sums + nums[i])   # 递归：下一层仍从 i 开始，允许重复选 nums[i]
                path.pop()                           # 撤销选择

        backtrack(0, [], 0)

        return output