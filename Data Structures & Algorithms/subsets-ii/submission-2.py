class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        output = []

        nums = sorted(nums)

        def backtrack(start, path):
            output.append(path[:])

            for i in range(start, len(nums)):

                if i > start and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])

                backtrack(i+1, path)

                path.pop()

        backtrack(0, [])

        return output



















        """
        题目：给定可能包含重复元素的数组 nums，返回所有可能的子集，结果中不能有重复子集。
        思路：回溯，在 LeetCode 78（子集）基础上加"排序 + 同层去重"，
             和 LeetCode 40（组合总和 II）的去重方式完全一样。
        为什么会重复：nums = [1, 2, 2]
            选 1 + 第 1 个 2 = [1, 2]
            选 1 + 第 2 个 2 = [1, 2]  ← 重复
        去重规则：同一层里相同的值只尝试第一次；不同层可以选相同的值，所以 [2, 2] 仍能得到
        例：nums = [1, 2, 2]
                        []
                    /        \
                  [1]        [2]          ← 第二个 2 在这一层被跳过
                   |          |
                 [1,2]      [2,2]
                   |
                [1,2,2]
            结果：[], [1], [1,2], [1,2,2], [2], [2,2]
        时间复杂度 O(n · 2^n)：最多 2^n 个子集，每个复制 O(n)
        空间复杂度 O(n)：递归深度和 path 长度（不算输出）

        小提示：
        - 必须先排序，相同的数相邻，nums[i] == nums[i-1] 才能判断出重复。
        - 去重条件是 i > start 而不是 i > 0：
          · i == start：本层第一个候选，即使和前一个数相同，前一个也是在上一层被选的，
            属于同一条路径，允许选（这样才能得到 [2, 2]）
          · i > start：同层前面已经用相同的值开过分支，再开会产生完全相同的子树，跳过
          一句话：同一树枝可以重复，同一树层不能重复。
        - "选或不选"的写法也能去重：选了 nums[i] 正常往下走；
          不选 nums[i] 时，要把后面所有和它相同的数一起跳过：
              def dfs(i, path):
                  if i == len(nums):
                      output.append(path[:])
                      return
                  path.append(nums[i])
                  dfs(i + 1, path)                  # 选 nums[i]
                  path.pop()
                  while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                      i += 1                        # 不选 nums[i]，相同的也都不选
                  dfs(i + 1, path)
        - 同系列去重：LeetCode 40（组合总和 II）、47（全排列 II）、15（三数之和）。
        """

        output = []   # 所有子集

        # 排序：让相同的数相邻，便于同层去重
        nums = sorted(nums)

        length = len(nums)

        def backtrack(start, path):
            """
            start：本层可以从 nums[start:] 中选数
            path ：当前已选的数，即当前节点对应的子集
            """
            # 每个节点都是一个合法子集，进入时就记录（必须复制）
            output.append(path[:])

            for i in range(start, length):
                # 同层去重：本层已经用相同的值开过分支，跳过
                # i > start 保证本层第一个数不受影响（允许和上一层选的数相同）
                if i > start and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])     # 做选择

                backtrack(i+1, path)     # 递归：下一个数只能从 i 之后选

                path.pop()               # 撤销选择

        backtrack(0, [])

        return output