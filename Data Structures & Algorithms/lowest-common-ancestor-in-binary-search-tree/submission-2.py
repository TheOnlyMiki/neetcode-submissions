# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # Method 2 - 迭代

        if not root or not p or not q:
            return None

        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root

        # Method 1 - 递归

        if not root or not p or not q:
            return None

        if p.val > q.val:
            p, q = q, p

        def findAncestor(node, p, q):
            if p.val > node.val:
                return findAncestor(node.right, p, q)
            
            if q.val < node.val:
                return findAncestor(node.left, p, q)

            return node

        return findAncestor(root, p, q)