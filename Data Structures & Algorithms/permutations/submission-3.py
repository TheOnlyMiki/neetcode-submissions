class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        """
        题目：给定不含重复数字的数组 nums，返回所有可能的全排列。
        思路：回溯。和子集 / 组合的区别在于"顺序有关"：
        - 组合：[1,2] 和 [2,1] 算同一个，所以下一层只从 start 之后选
        - 排列：[1,2] 和 [2,1] 不同，所以每一层都要从头（下标 0）开始选，
          但同一个数在一条路径上只能用一次 → 用 visit 数组记录哪些数已经在 path 里
        只在 path 长度等于 n 时（叶子节点）记录结果。
        例：nums = [1, 2, 3]
                           []
                   /       |       \
                 [1]      [2]      [3]
                /   \    /   \    /   \
             [1,2][1,3][2,1][2,3][3,1][3,2]
               |    |    |    |    |    |
            [1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]
        时间复杂度 O(n · n!)：共 n! 个排列，每个复制 O(n)
        空间复杂度 O(n)：递归深度、path、visit 都是 O(n)（不算输出）

        小提示：
        - visit[i] is False 可以简写成 not visit[i]，更符合 Python 习惯。
        - 不用 visit 的写法：直接判断 if nums[i] in path，但 in 是 O(n)，
          整体变慢，而且 nums 有重复元素时就不对了。
        - 交换法（不需要 visit 和 path）：第 start 位依次和后面每个位置交换，
          递归处理 start + 1，回溯时再换回来：
              def backtrack(start):
                  if start == len(nums):
                      output.append(nums[:])
                      return
                  for i in range(start, len(nums)):
                      nums[start], nums[i] = nums[i], nums[start]
                      backtrack(start + 1)
                      nums[start], nums[i] = nums[i], nums[start]
          缺点是输出顺序不是字典序。
        - 如果 nums 有重复元素（LeetCode 47 全排列 II）：先排序，同层去重条件为
              if i > 0 and nums[i] == nums[i-1] and not visit[i-1]: continue
          含义：相同的数必须按顺序使用，前一个相同的数没用过（在同一层被撤销了）时，
          当前这个也不能用，否则会产生重复排列。
        - 标准库：list(itertools.permutations(nums)) 可直接生成，但面试一般要求手写。
        """

        output = []   # 所有排列

        length = len(nums)

        def backtrack(path, visit):
            """
            path ：当前已排好的部分排列
            visit：visit[i] 为 True 表示 nums[i] 已经在 path 中
            """
            # 所有数都已放入：得到一个完整排列，记录（必须复制）
            if len(path) == length:
                output.append(path[:])
                return

            # 排列与顺序有关，每一层都从下标 0 开始尝试
            for i in range(length):
                # 只能选还没用过的数
                if visit[i] is False:
                    visit[i] = True          # 做选择：标记已使用
                    path.append(nums[i])

                    backtrack(path, visit)   # 递归：填下一个位置

                    path.pop()               # 撤销选择：恢复 path 和 visit
                    visit[i] = False

        backtrack([], [False] * length)

        return output