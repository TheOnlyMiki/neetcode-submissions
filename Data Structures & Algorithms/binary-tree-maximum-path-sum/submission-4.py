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

            left_single_sums, left_merge_sums = dfs(node.left)
            right_single_sums, right_merge_sums = dfs(node.right)

            current_single_sums = node.val + max(left_single_sums, right_single_sums, 0)
            current_merge_sums = node.val + left_single_sums + right_single_sums
            current_merge_sums = max(left_merge_sums, right_merge_sums, current_merge_sums, current_single_sums)

            return current_single_sums, current_merge_sums

        return max(dfs(root))