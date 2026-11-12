# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        题目：翻转二叉树（镜像），即交换每个节点的左右子树。
        核心：只要每个节点都交换一次左右孩子，整棵树就翻转了，
             遍历顺序（BFS / 前序 / 后序）都可以，区别只在怎么访问到所有节点。
        """

        # ==================== Method 3 - BFS（按层遍历） ====================
        # 时间复杂度 O(n)：每个节点访问一次
        # 空间复杂度 O(w)：w 为树的最大宽度，最坏（完全二叉树最后一层）约 n / 2

        if not root:
            return None

        # 当前层的所有节点（虽然叫 stack，实际是按层处理的列表）
        level = [root]

        while level:
            next_level = []   # 收集下一层的节点

            for node in level:
                # 子节点可能为 None，这里跳过
                if node:
                    # 交换左右子树
                    node.left, node.right = node.right, node.left
                    # 把孩子加入下一层（包括 None，靠上面的 if 过滤）
                    next_level += [node.left, node.right]

            # 进入下一层
            level = next_level

        return root

        # ==================== Method 2 - DFS 迭代（显式栈） ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(n)，空间复杂度 O(h)：h 为树高，最坏（链状树）为 O(n)
        # 用栈模拟递归，访问顺序是前序（根 → 子树）

        if not root:
            return None

        stack = [root]

        while stack:
            node = stack.pop()   # 后进先出，深度优先

            # 交换当前节点的左右子树
            node.left, node.right = node.right, node.left

            # 只把非空孩子压栈，后续再处理它们
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root

        # ==================== Method 1 - DFS 递归 ====================
        # 时间复杂度 O(n)，空间复杂度 O(h)（递归栈深度）
        # 递归定义：翻转一棵树 = 交换根的左右子树 + 分别翻转左、右子树

        # 递归终止：空树无需翻转
        if not root:
            return None

        # 先交换当前节点的左右子树（前序位置）
        root.left, root.right = root.right, root.left

        # 再递归翻转左右子树（此时的 left 其实是原来的 right，不影响结果）
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root