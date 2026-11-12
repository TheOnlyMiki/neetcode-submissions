# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # DFS - inorder
        
        # DFS - inorder

        record = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            record.append(node.val)
            dfs(node.right)

        dfs(root)

        return record[k-1]
