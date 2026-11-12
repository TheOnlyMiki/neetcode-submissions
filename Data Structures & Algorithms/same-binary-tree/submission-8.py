# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True

        if p is None or q is None or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


























        """
        题目：判断两棵二叉树是否完全相同（结构相同且对应节点值相同）。
        核心：同步遍历两棵树，每次比较"对应位置"的一对节点：
        - 都为空 → 这一处相同，跳过
        - 一个空一个不空，或值不同 → 不相同
        - 都不空且值相同 → 继续比较它们的左孩子对、右孩子对
        三种写法只是遍历顺序不同，比较逻辑完全一样。
        """

        # ==================== Method 3 - BFS（按层同步遍历） ====================
        # 时间复杂度 O(min(m, n))：最多比较到较小那棵树的所有节点就能得出结论
        # 空间复杂度 O(w)：w 为树的最大宽度

        # 当前层的所有"对应位置节点对"，每个元素是 (p 中的节点, q 中的节点)
        # 打包成元组后两边天然对齐，不需要靠下标维护
        level = [(p, q)]

        while level:
            next_level = []   # 收集下一层的节点对

            for p_node, q_node in level:
                # 都为空：这一位置相同，也没有孩子要继续比较
                if p_node is None and q_node is None:
                    continue

                # 一个空一个不空（结构不同），或值不同
                if p_node is None or q_node is None or p_node.val != q_node.val:
                    return False

                # 当前一对相同，把左孩子对、右孩子对加入下一层
                next_level += [(p_node.left, q_node.left), (p_node.right, q_node.right)]

            # 进入下一层
            level = next_level

        # 所有对应位置都比较过且相同
        return True

        # ==================== Method 2 - DFS 迭代（栈中存节点对） ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(min(m, n))，空间复杂度 O(h)
        # 把"对应位置的一对节点"打包成元组压栈，天然保证两边对齐

        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            # 都为空：这一对相同，跳过
            if not node1 and not node2:
                continue

            # 一个空一个不空，或值不同
            if not node1 or not node2 or node1.val != node2.val:
                return False

            # 当前一对相同，继续比较左孩子对、右孩子对
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))

        return True

        # ==================== Method 1 - DFS 递归 ====================
        # 时间复杂度 O(min(m, n))，空间复杂度 O(h)（递归栈深度）
        # 递归定义：两棵树相同 = 根相同 + 左子树相同 + 右子树相同

        # 都为空：相同（递归终止）
        if not p and not q:
            return True

        # 都不空且根值相同：再分别比较左右子树
        # and 会短路，左子树不同时直接返回 False，不再比较右子树
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # 一个空一个不空，或根值不同
        else:
            return False