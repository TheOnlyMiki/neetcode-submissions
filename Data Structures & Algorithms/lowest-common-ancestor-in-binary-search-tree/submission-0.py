# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val > q.val:
            p, q = q, p

        def findAncestor(node, p, q):
            if p.val > node.val:
                return findAncestor(node.right, p, q)
            
            if q.val < node.val:
                return findAncestor(node.left, p, q)

            return node

        return findAncestor(root, p, q)