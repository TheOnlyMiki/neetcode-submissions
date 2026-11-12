# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        题目：找 BST 中第 k 小的元素（k 从 1 开始）。
        核心：BST 的中序遍历（左 → 根 → 右）结果严格递增，
             所以中序遍历访问到的第 k 个节点就是第 k 小的元素。

        提示：Method 1 即使 k = 1 也会遍历完整棵树。可以改成递归时也计数，
            数到第 k 个就记录结果并停止往下递归，这样时间也能降到 O(h + k)，
            空间降到 O(h)。
            这题的进阶问题是：如果 BST 经常插入、删除，又要频繁查询第 k 小，
            怎么优化？常见回答是在每个节点额外存"以它为根的子树节点数"。
            查询时比较 k 和左子树大小：k 小于等于左子树大小就往左走，
            正好等于左子树大小加一就是当前节点，否则减去左子树大小加一后往右走。
            这样每次查询只需 O(h)。
        """

        # ==================== Method 2 - 中序遍历（迭代，提前结束） ====================
        # 时间复杂度 O(h + k)：先一路向左走到最小值（约 h 步），再往后访问 k 个节点就停
        # 空间复杂度 O(h)：栈中最多存一条从根到叶的路径

        stack = []
        current = root

        while current or stack:
            # 一路向左，把沿途节点压栈（越往左值越小）
            while current:
                stack.append(current)
                current = current.left

            # 弹出栈顶：当前未访问节点中最小的那个
            node = stack.pop()

            # 每访问一个节点，k 减 1；减到 0 说明这正是第 k 小的
            k -= 1

            if k == 0:
                return node.val   # 找到就立刻返回，不用遍历整棵树

            # 转向右子树，下一轮会对右子树重复"一路向左"
            current = node.right

        # 题目保证 1 <= k <= n，不会走到这里
        return -1

        # ==================== Method 1 - 中序遍历（递归，存下全部结果） ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(n)：遍历整棵树
        # 空间复杂度 O(n)：record 存所有节点值，另有 O(h) 递归栈
        # 思路：先把中序遍历的完整有序序列存下来，再直接取下标 k - 1

        record = []   # 中序遍历结果，严格递增

        def dfs(node):
            if node is None:
                return

            dfs(node.left)            # 先遍历左子树（更小的值）
            record.append(node.val)   # 再访问根
            dfs(node.right)           # 最后遍历右子树（更大的值）

        dfs(root)

        # 第 k 小对应下标 k - 1
        return record[k-1]