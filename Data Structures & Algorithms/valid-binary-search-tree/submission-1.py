# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # BFS

        level = [(root, -float('inf'), float('inf'))]

        while level:
            next_level = []

            for node, min_val, max_val in level:
                if node.val <= min_val or node.val >= max_val:
                    return False

                if node.left:
                    next_level.append((node.left, min_val, node.val))
                if node.right:
                    next_level.append((node.right, node.val, max_val))

            level = next_level

        return True
        
        # DFS

        def dfs(node, min_val, max_val):
            if node is None:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        return dfs(root, -float('inf'), float('inf'))