# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # DFS - inorder
        
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            node = stack.pop()
            k -= 1

            if k == 0:
                return node.val

            current = node.right

        return -1

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
