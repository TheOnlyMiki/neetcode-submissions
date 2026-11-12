# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        题目：二叉树的直径 = 任意两个节点之间最长路径的"边数"，路径不一定经过根节点。
        关键观察：任何一条路径都有一个"最高点"节点，
                 经过该节点的最长路径长度 = 左子树高度 + 右子树高度。
        所以对每个节点都要知道：
        - 它的高度（给父节点用）
        - 以它为根的子树内的最大直径（最终答案）
        这两个量都依赖左右孩子的结果 → 后序遍历（先处理孩子，再处理自己）
        """

        # ==================== Method 2 - 递归 + 全局最大值 ====================
        # 时间复杂度 O(n)：每个节点访问一次
        # 空间复杂度 O(h)：递归栈深度，h 为树高，最坏（链状树）为 O(n)
        # 思路：递归函数只负责返回高度，直径在递归过程中"顺手"更新到全局变量里

        # 记录遍历过程中见过的最大直径
        self.diameter = 0

        def height(node):
            """返回以 node 为根的子树高度（节点数），空节点高度为 0"""
            if not node:
                return 0

            # 后序遍历：先拿到左右子树的高度
            left = height(node.left)
            right = height(node.right)

            # 经过当前节点的最长路径 = 左高度 + 右高度（边数）
            # 每个节点都可能是某条最长路径的"最高点"，所以每个节点都要比较一次
            self.diameter = max(self.diameter, left + right)

            # 返回给父节点：当前节点高度 = 较高的子树高度 + 自己
            return 1 + max(left, right)

        height(root)
        return self.diameter

        # ==================== Method 1 - 迭代后序遍历 + 哈希表 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(n)：每个节点入栈、出栈各一次
        # 空间复杂度 O(n)：record 存所有节点的结果；栈深度 O(h)
        # 优点：不用递归，树很深时不会栈溢出；也不需要全局变量

        # 空树时栈为空，直接走到最后返回 record[None][1] = 0
        stack = [root] if root else []

        # record[node] = (高度, 子树内最大直径)
        # 高度定义为"从该节点往下最长路径上的节点数"，空节点高度为 0
        # 预先放入 None，这样叶子节点查孩子时不用特判
        record = {None: (0, 0)}

        while stack:
            # 先只"看"栈顶，不弹出：要确认它的孩子都处理完了才能处理它
            node = stack[-1]

            # ---------- 左孩子存在且还没算过 → 先去处理左子树 ----------
            if node.left and node.left not in record:
                stack.append(node.left)

            # ---------- 左边处理完了，右孩子存在且还没算过 → 去处理右子树 ----------
            elif node.right and node.right not in record:
                stack.append(node.right)

            # ---------- 左右孩子都已算好（或不存在）→ 处理当前节点 ----------
            else:
                node = stack.pop()

                # 取出左右孩子的结果（空孩子查到的是 (0, 0)）
                left_height, left_diameter = record[node.left]
                right_height, right_diameter = record[node.right]

                record[node] = (
                    # 当前节点高度 = 较高的子树高度 + 自己这一个节点
                    1 + max(left_height, right_height),

                    # 当前子树内的最大直径取三者最大：
                    # 1. 经过当前节点的路径：左高度 + 右高度
                    #    （高度按节点数算，左右各 h 个节点到当前节点正好 h 条边）
                    # 2. 完全在左子树内部的最大直径
                    # 3. 完全在右子树内部的最大直径
                    max(left_height + right_height, left_diameter, right_diameter)
                )

        # 根节点子树内的最大直径就是整棵树的直径
        return record[root][1]