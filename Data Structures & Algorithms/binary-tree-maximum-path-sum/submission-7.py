# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        题目：二叉树中的最大路径和。路径是任意节点序列，相邻节点之间有边相连，
             每个节点最多出现一次，至少包含一个节点，不一定经过根节点。
        核心观察（和二叉树直径同一个框架）：
        任何一条路径都有一个"最高点"节点，路径在这个节点处"拐弯"：
            最高点 + 左边往下的一条链 + 右边往下的一条链
        所以对每个节点要算两个量：
        - single（单链）：从当前节点出发，只往下走一条分支的最大和
                         → 交给父节点用，因为父节点只能接上它的一条分支（不能分叉）
        - merge（全局最优）：以当前节点为根的子树内，任意路径的最大和
                         → 最终答案
        这两个量都依赖左右孩子的结果 → 后序遍历
        时间复杂度 O(n)：每个节点访问一次
        空间复杂度 O(h)：递归栈深度

        例：      -10
                 /   \
                9     20
                     /  \
                    15   7
            节点 20：single = 20 + max(15, 7) = 35，经过它拐弯 = 15 + 20 + 7 = 42
            节点 -10：经过它拐弯 = 9 + (-10) + 35 = 34 < 42
            答案为 42（路径 15 → 20 → 7，不经过根）

        小提示：
        - 负数的处理是本题关键：子链贡献为负时宁可不要，所以 single 里和 0 取 max。
          拐弯那一项 node.val + left_single + right_single 没有和 0 取 max，
          看起来可能把负的分支加进来，但不会出错：
          · 两边都为正 → 这一项就是真正的最优拐弯路径
          · 只有一边为正 / 两边都不为正 → 最优路径就是 current_single，已经被包含在 max 里
          所以四项取 max 后结果一定正确。
        - 空节点返回 single = 0 而不是 -inf：叶子节点计算拐弯时 val + 0 + 0 = val，正好是它自己；
          merge 返回 -inf 是为了保证空子树永远不会被选为答案（全是负数的树也能正确处理）。
        - current_merge 里已经包含了 current_single，所以 merge >= single 恒成立，
          最后的 max(dfs(root)) 可以直接写成 dfs(root)[1]。
        - 更常见的写法是用一个全局变量记录答案，递归函数只返回 single：
              self.best = -float('inf')
              def dfs(node):
                  if node is None:
                      return 0
                  left = max(dfs(node.left), 0)    # 负贡献直接舍弃
                  right = max(dfs(node.right), 0)
                  self.best = max(self.best, node.val + left + right)  # 在当前节点拐弯
                  return node.val + max(left, right)                   # 只能带一条分支给父节点
              dfs(root)
              return self.best
          和二叉树直径（LeetCode 543）的递归写法几乎一模一样，只是"高度"换成了"路径和"。
        """

        def dfs(node):
            """返回 (single, merge)：
            single：从 node 出发往下走一条分支的最大路径和
            merge ：以 node 为根的子树内任意路径的最大和
            """
            # 空节点：单链贡献为 0（相当于不往这边走）；
            # 子树内没有任何路径，最优值设为 -inf，保证不会被选中
            if node is None:
                return 0, -float('inf')

            # 后序遍历：先拿到左右子树的结果
            left_single, left_merge = dfs(node.left)
            right_single, right_merge = dfs(node.right)

            # 单链：当前节点 + 左右两条链中较大的那条；两条都为负就只要自己（和 0 比较）
            current_single = node.val + max(left_single, right_single, 0)

            # 在当前节点拐弯：左链 + 当前节点 + 右链
            current_merge = node.val + left_single + right_single

            # 子树内的最优路径取四者最大：
            # 1. 完全在左子树内部的最优路径
            # 2. 完全在右子树内部的最优路径
            # 3. 在当前节点拐弯的路径
            # 4. 以当前节点为起点往下的单链（处理有负分支时拐弯不划算的情况）
            current_merge = max(left_merge, right_merge, current_merge, current_single)

            return current_single, current_merge

        # merge 一定 >= single，这里取 max 等价于取 merge
        return max(dfs(root))