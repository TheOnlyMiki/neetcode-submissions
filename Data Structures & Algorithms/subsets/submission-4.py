class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        output = []

        def backtrack(start, path):
            output.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])

                backtrack(i+1, path)

                path.pop()

        backtrack(0, [])

        return output

















        """
        题目：给定互不相同的整数数组 nums，返回所有可能的子集（幂集），不能有重复子集。
        思路：回溯。把"构造子集"看成一棵树：
        - 每个节点代表一个子集（从根到该节点路径上选的数）
        - 从某个节点往下，只能选"下标比上一个选的数更大"的数，避免 [1,2] 和 [2,1] 重复
        - 树上的每个节点都是一个合法子集，所以一进入就记录，而不是只在叶子记录
        例：nums = [1, 2, 3]
                        []
                   /     |     \
                 [1]    [2]    [3]
                /   \     |
            [1,2] [1,3] [2,3]
              |
           [1,2,3]
            按访问顺序输出：[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]
        时间复杂度 O(n · 2^n)：共 2^n 个子集，每个复制进结果需要 O(n)
        空间复杂度 O(n)：递归深度和 path 长度最多 n（不算输出）

        小提示：
        - output.append(path[:]) 必须复制：path 是同一个列表，之后会被不断修改，
          直接 append(path) 存的是引用，最后结果里全都会变成空列表。
        - 回溯三步模板：做选择（append）→ 递归 → 撤销选择（pop），
          LeetCode 39（组合总和）, 46（全排列）, 77（组合）都是这个框架，区别只在：
          · 何时记录结果（每个节点 / 叶子 / 满足条件时）
          · 下一层从哪里开始选（i + 1 不可重复使用 / i 可重复使用 / 0 排列）
        - 另一种回溯思路："选或不选"二叉决策树，每个数都决定选或不选，叶子才记录：
              def dfs(i, path):
                  if i == len(nums):
                      output.append(path[:])
                      return
                  path.append(nums[i])
                  dfs(i + 1, path)      # 选 nums[i]
                  path.pop()
                  dfs(i + 1, path)      # 不选 nums[i]
        - 迭代写法：每加入一个新数，就把它加到已有的每个子集上，子集数量翻倍：
              output = [[]]
              for num in nums:
                  output += [subset + [num] for subset in output]
        - 位运算写法：n 个数的子集与 0 ~ 2^n - 1 的二进制一一对应，第 j 位为 1 表示选 nums[j]。
        - 如果 nums 有重复元素（LeetCode 90 子集 II）：先排序，
          同一层里遇到和前一个相同的数就跳过：if i > start and nums[i] == nums[i-1]: continue
        """

        output = []   # 所有子集

        def backtrack(start, path):
            """
            start：本层可以从 nums[start:] 中选数（保证选的下标递增，避免重复子集）
            path ：当前已选的数，即当前节点对应的子集
            """
            # 每个节点都是一个合法子集，进入时就记录（必须复制）
            output.append(path[:])

            # 依次尝试把 nums[start], nums[start+1], ... 加入子集
            for i in range(start, len(nums)):
                path.append(nums[i])     # 做选择
                backtrack(i+1, path)     # 递归：下一个数只能从 i 之后选
                path.pop()               # 撤销选择，回到当前节点，尝试下一个数

        backtrack(0, [])

        return output