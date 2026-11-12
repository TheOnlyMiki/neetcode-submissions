# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node is None:
                return 0, -float('inf')

            left_single, left_merge = dfs(node.left)
            right_single, right_merge = dfs(node.right)

            current_single = node.val + max(left_single, right_single, 0)
            current_merge = node.val + left_single + right_single
            current_merge = max(left_merge, right_merge, current_merge, current_single)

            return current_single, current_merge

        return max(dfs(root))