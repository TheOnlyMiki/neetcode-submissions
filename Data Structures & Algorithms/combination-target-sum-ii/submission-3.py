class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        题目：给定可能包含重复数字的正整数数组 candidates 和目标值 target，
             找出所有和为 target 的组合，每个数字在每个组合中只能使用一次，
             结果中不能包含重复组合。
        思路：回溯，在 LeetCode 39 基础上改两处：
        1. 下一层从 i + 1 开始 → 每个位置的数只能用一次
        2. 排序后"同一层"跳过相同的数 → 去掉重复组合
        为什么会出现重复组合：candidates = [1, 1, 2]，target = 3
            选第 1 个 1 + 2 = [1, 2]
            选第 2 个 1 + 2 = [1, 2]  ← 重复
        去重规则：在同一层（同一个 for 循环）里，相同的值只尝试第一次
                但"不同层"可以选相同的值，所以 [1, 1, ...] 这样的组合仍然能得到
        例：candidates = [10, 1, 2, 7, 6, 1, 5]，target = 8
            排序后 [1, 1, 2, 5, 6, 7, 10]
            结果：[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]
        时间复杂度 O(2^n · n)：最坏每个数选或不选，每个结果复制 O(n)
        空间复杂度 O(n)：递归深度和 path 长度（排序另需 O(n)）

        小提示：
        - 去重条件是 i > start 而不是 i > 0，这是本题最关键的细节：
          · i == start：这是本层第一个候选，即使它和前一个数相同，
            前一个数也是在"上一层"被选的（属于同一条路径），允许选，比如 [1, 1, 6]
          · i > start：同一层里前面已经用相同的值开过一个分支，再开就会产生完全相同的子树，跳过
          一句话：同一树枝可以重复，同一树层不能重复。
        - 排序有两个作用：让相同的数相邻（才能用 candidates[i] == candidates[i-1] 去重），
          并让后面的数更大（超过 target 时可以直接 break 剪枝）。
        - 两个判断的顺序可以互换，都不影响正确性。
        - 这个"排序 + 同层跳过相同值"的去重技巧通用于：
          LeetCode 90（子集 II）、47（全排列 II）、15（三数之和）。
        """

        output = []   # 所有满足条件的组合

        # 排序：让相同的数相邻，便于同层去重；同时让数字递增，便于剪枝
        candidates = sorted(candidates)

        def backtrack(start, path, sums):
            """
            start：本层可以从 candidates[start:] 中选数
            path ：当前已选的数
            sums ：当前已选数的和
            """
            # 和恰好等于目标：记录组合（必须复制）
            # 全是正数，再往下选只会更大，直接返回
            if sums == target:
                output.append(path[:])
                return

            for i in range(start, len(candidates)):
                # 同层去重：本层已经用相同的值开过分支，跳过
                # i > start 保证本层第一个数不受影响（允许和上一层选的数相同）
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                # 剪枝：已排序，当前数加上就超过目标，后面更大的数也一定超过，整层结束
                if sums + candidates[i] > target:
                    break

                path.append(candidates[i])                       # 做选择
                backtrack(i+1, path, sums + candidates[i])       # 递归：每个数只能用一次，从 i + 1 开始
                path.pop()                                       # 撤销选择

        backtrack(0, [], 0)

        return output