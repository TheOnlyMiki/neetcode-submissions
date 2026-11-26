# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return -float('inf'), -float('inf')

            left, left_max = dfs(node.left)

            right, right_max = dfs(node.right)

            single_self_sums = max(left, right, 0) + node.val

            include_self_sums = max(left, 0) + max(right, 0) + node.val

            return single_self_sums, max(include_self_sums, left_max, right_max)

        _, max_sums = dfs(root)

        return max_sums
        