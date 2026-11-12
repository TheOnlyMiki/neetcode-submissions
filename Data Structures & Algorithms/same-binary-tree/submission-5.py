# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # BFS

        level_p = [p]
        level_q = [q]

        while level_p and level_q:
            next_level_p, next_level_q = [], []

            for i in range(len(level_p)):
                p_node, q_node = level_p[i], level_q[i]

                if p_node is None and q_node is None:
                    continue

                if p_node is None or q_node is None or p_node.val != q_node.val:
                    return False

                next_level_p += [p_node.left, p_node.right]
                next_level_q += [q_node.left, q_node.right]

            level_p, level_q = next_level_p, next_level_q

        return True

        # DFS - 迭代

        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False

            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))

        return True
        
        # DFS

        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        else:
            return False