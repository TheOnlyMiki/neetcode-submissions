# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        题目：在二叉搜索树（BST）中找 p、q 的最近公共祖先（LCA）。
             一个节点也可以是它自己的祖先。
        利用 BST 性质：左子树所有值 < 根 < 右子树所有值
        从根往下走，对当前节点 node：
        - p、q 都比 node 大 → 两者都在右子树，LCA 也在右子树
        - p、q 都比 node 小 → 两者都在左子树，LCA 也在左子树
        - 否则（一个在左一个在右，或其中一个就是 node）→ node 就是"分叉点"，即 LCA
        """

        # ==================== Method 2 - 迭代 ====================
        # 时间复杂度 O(h)：每层只往下走一步，h 为树高（平衡时 O(log n)，最坏 O(n)）
        # 空间复杂度 O(1)

        if not root or not p or not q:
            return None

        while root:
            # 都在右边，往右走
            if p.val > root.val and q.val > root.val:
                root = root.right

            # 都在左边，往左走
            elif p.val < root.val and q.val < root.val:
                root = root.left

            # p、q 分在两侧，或某一个就是当前节点 → 找到分叉点
            else:
                return root

        # 题目保证 p、q 都在树中，一定会在循环内返回，不会走到这里

        # ==================== Method 1 - 递归 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(h)，空间复杂度 O(h)（递归栈深度）

        if not root or not p or not q:
            return None

        # 保证 p.val <= q.val，这样后面只需判断两个条件：
        # - 较小的 p 都比 node 大 → 两个都比 node 大
        # - 较大的 q 都比 node 小 → 两个都比 node 小
        if p.val > q.val:
            p, q = q, p

        def findAncestor(node, p, q):
            # 较小值都在右边 → 两者都在右子树
            if p.val > node.val:
                return findAncestor(node.right, p, q)

            # 较大值都在左边 → 两者都在左子树
            if q.val < node.val:
                return findAncestor(node.left, p, q)

            # p.val <= node.val <= q.val → node 就是分叉点
            return node

        return findAncestor(root, p, q)