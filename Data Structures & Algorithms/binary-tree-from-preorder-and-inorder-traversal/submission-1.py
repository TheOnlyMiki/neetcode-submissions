# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_i = {val:i for i,val in enumerate(inorder)}
        self.preorder_i = 0
        
        def dfs(l, r):
            if l > r:
                return None

            root = preorder[self.preorder_i]

            self.preorder_i += 1

            mid = inorder_i[root]

            root = TreeNode(val=root)

            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)

            return root

        return dfs(0, len(preorder)-1)