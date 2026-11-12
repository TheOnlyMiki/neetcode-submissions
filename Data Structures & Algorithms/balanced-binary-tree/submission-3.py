# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        题目：判断二叉树是否是平衡二叉树，
             即每个节点的左右子树高度差的绝对值都不超过 1。
        注意：要求"每个节点"都满足，不只是根节点。
        思路：判断一个节点需要左右子树的高度 → 后序遍历（先孩子，后自己），
             自底向上计算高度，途中一旦发现不平衡就提前结束。
        """

        # ==================== Method 2 - 递归，用 -1 标记不平衡 ====================
        # 时间复杂度 O(n)：每个节点访问一次
        # 空间复杂度 O(h)：递归栈深度，最坏（链状树）为 O(n)
        # 思路：递归函数返回子树高度；若子树已经不平衡，返回 -1 作为信号，
        #      一路向上传递，不再继续计算

        def height(node):
            """平衡时返回高度（节点数），不平衡时返回 -1"""
            if not node:
                return 0

            # 先算左子树，若已不平衡直接向上返回，右子树都不用算（剪枝）
            left = height(node.left)
            if left == -1:
                return -1

            right = height(node.right)
            if right == -1:
                return -1

            # 当前节点不平衡
            if abs(left - right) > 1:
                return -1

            # 平衡，返回当前节点高度
            return 1 + max(left, right)

        return height(root) != -1

        # ==================== Method 1 - 迭代后序遍历 + 哈希表 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(n)：每个节点入栈、出栈各一次
        # 空间复杂度 O(n)：record 存所有节点的高度；栈深度 O(h)
        # 优点：不用递归，树很深时不会栈溢出

        # 空树时栈为空，直接返回 True（空树是平衡的）
        stack = [root] if root else []

        # record[node] = 以 node 为根的子树高度（节点数）
        # 预先放入 None → 0，叶子节点查孩子时不用特判
        record = {None: 0}

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

                left_height = record[node.left]
                right_height = record[node.right]

                # 当前节点左右高度差超过 1，整棵树就不平衡，提前结束
                if abs(left_height - right_height) > 1:
                    return False

                # 当前节点平衡，记录高度供父节点使用
                record[node] = 1 + max(left_height, right_height)

        # 所有节点都检查过且都平衡
        return True