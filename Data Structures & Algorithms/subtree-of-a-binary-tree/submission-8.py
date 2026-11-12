# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # Method 2 - 走一遍存每个node字符串，然后再匹配

        if subRoot is None:
            return True

        if root is None:
            return False

        res = []

        def dfs(node):
            if node is None:
                res.append("$#")
                return

            res.append("$")
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        root_sentence = "".join(res)

        res = []

        dfs(subRoot)

        subRoot_sentence = "".join(res)

        return subRoot_sentence in root_sentence

        # Method 1 - BFS， 一个个node检索

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

        level = [root]

        while level:
            next_level = []

            for node in level:
                if isSameTree(node, subRoot):
                    return True

                if node:
                    next_level += [node.left, node.right]

            level = next_level

        return False

        