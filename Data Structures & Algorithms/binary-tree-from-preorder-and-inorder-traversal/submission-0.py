# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        record = {
            val: i for i, val in enumerate(inorder)
        }

        self.preorder_i = 0

        def dfs(left, right):
            if left > right:
                return None

            root_val = preorder[self.preorder_i]
            self.preorder_i += 1

            root = TreeNode(val=root_val)
            mid = record[root_val]

            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1, right)

            return root

        return dfs(0, len(preorder) - 1)