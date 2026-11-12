# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if subRoot is None:
            return True

        if root is None:
            return False
        
        def isSameTree(p, q):
            level = [(p, q)]

            while level:
                next_level = []

                for (p_node, q_node) in level:
                    if p_node is None and q_node is None:
                        continue
                    
                    if p_node is  None or q_node is None or q_node.val != p_node.val:
                        return False

                    next_level +=[(p_node.left, q_node.left), (p_node.right, q_node.right)]

                level = next_level

            return True

        result = False

        stack = [root]

        while stack:
            node = stack.pop()

            result = (isSameTree(node, subRoot) or result)

            if node:
                stack += [node.left, node.right]

        return result

        