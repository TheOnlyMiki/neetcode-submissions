# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # BFS

        level = [(root, root.val)]

        output = 0

        while level:
            next_level = []

            for node, max_val in level:
                if node.val >= max_val:
                    output += 1
                    max_val = node.val

                if node.left:
                    next_level.append((node.left, max_val))

                if node.right:
                    next_level.append((node.right, max_val))

            level = next_level

        return output

        # DFS
        
        def dfs(node, max_val):
            if node is None:
                return 0

            good_node = 0
            if node.val >= max_val:
                good_node = 1 
                max_val = node.val

            num_good_nodes = dfs(node.left, max_val) + dfs(node.right, max_val)

            return good_node + num_good_nodes

        return dfs(root, root.val)
        