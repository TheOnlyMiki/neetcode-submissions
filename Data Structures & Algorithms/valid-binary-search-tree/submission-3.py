# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        题目：判断二叉树是否是有效的二叉搜索树（BST）。
             BST 定义：左子树"所有"节点 < 根 < 右子树"所有"节点，且左右子树也都是 BST。
        常见错误：只比较节点和它的直接孩子。
        例：    5
               / \
              4   6
                 / \
                3   7
            每个节点和孩子比都没问题，但 3 在 5 的右子树里却比 5 小 → 不是 BST
        正确思路：给每个节点维护一个合法区间 (min_val, max_val)，从上往下传：
        - 往左走：上界收紧为当前节点值 → (min_val, node.val)
        - 往右走：下界收紧为当前节点值 → (node.val, max_val)
        节点值必须严格落在区间内（BST 不允许重复值）。
        """

        # ==================== Method 3 - 中序遍历（迭代） ====================
        # 时间复杂度 O(n)，空间复杂度 O(h)
        # BST 的中序遍历结果严格递增，只要发现当前值 <= 上一个值就不是 BST

        stack = []
        current = root
        pre_val = -float('inf')   # 上一个访问的节点值

        while current or stack:
            # 一路向左压栈
            while current:
                stack.append(current)
                current = current.left

            # 访问当前节点
            current = stack.pop()

            # 不是严格递增 → 不是 BST
            if current.val <= pre_val:
                return False
            pre_val = current.val

            # 转向右子树
            current = current.right

        return True

        # ==================== Method 2 - BFS（节点和合法区间打包传递） ====================
        # 时间复杂度 O(n)：每个节点访问一次
        # 空间复杂度 O(w)：w 为树的最大宽度
        # 题目保证树至少有一个节点，所以可以直接访问 node.val

        # 每个元素为 (节点, 下界, 上界)，根节点没有限制，区间为 (-inf, +inf)
        level = [(root, -float('inf'), float('inf'))]

        while level:
            next_level = []

            for node, min_val, max_val in level:
                # 不在开区间 (min_val, max_val) 内 → 违反 BST 性质
                # 用 <= 和 >= 是因为 BST 要求严格大于/小于，等于也不合法
                if node.val <= min_val or node.val >= max_val:
                    return False

                # 左孩子：继承下界，上界收紧为当前节点值
                if node.left:
                    next_level.append((node.left, min_val, node.val))

                # 右孩子：下界收紧为当前节点值，继承上界
                if node.right:
                    next_level.append((node.right, node.val, max_val))

            level = next_level

        # 所有节点都在各自合法区间内
        return True

        # ==================== Method 1 - DFS 递归 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(n)，空间复杂度 O(h)（递归栈深度）
        # 递归定义：以 node 为根的子树是有效 BST
        #         = node 在合法区间内 + 左子树在 (min, node.val) 内有效 + 右子树在 (node.val, max) 内有效

        def dfs(node, min_val, max_val):
            # 空树是有效 BST
            if node is None:
                return True

            # 当前节点不在合法区间内
            if node.val <= min_val or node.val >= max_val:
                return False

            # 左右子树分别带着收紧后的区间继续检查
            # and 会短路，左子树不合法时不再检查右子树
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        # 根节点区间为 (-inf, +inf)
        return dfs(root, -float('inf'), float('inf'))