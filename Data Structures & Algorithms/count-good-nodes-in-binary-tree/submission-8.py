# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        题目：统计二叉树中"好节点"的个数。
             好节点：从根到该节点的路径上，没有任何节点的值比它大
             （即它的值 >= 路径上所有祖先的值）。
        核心：遍历时把"根到当前节点路径上的最大值"一起往下传，
             当前节点值 >= 这个最大值，就是好节点。
        注意：最大值是沿"路径"传递的，不同分支互不影响，
             所以要跟着节点一起传，不能用一个全局变量。
        """

        # ==================== Method 2 - BFS（节点和路径最大值打包传递） ====================
        # 时间复杂度 O(n)：每个节点访问一次
        # 空间复杂度 O(w)：w 为树的最大宽度
        # 题目保证树至少有一个节点，所以可以直接访问 root.val

        # 每个元素为 (节点, 根到它父节点路径上的最大值)
        # 根节点没有祖先，用自己的值初始化，保证根一定是好节点
        level = [(root, root.val)]

        output = 0   # 好节点个数

        while level:
            next_level = []

            for node, max_val in level:
                # 当前节点不小于路径上的最大值 → 好节点
                # 同时它成为新的路径最大值，传给孩子
                if node.val >= max_val:
                    output += 1
                    max_val = node.val

                # 把孩子和"包含当前节点在内"的路径最大值一起加入下一层
                if node.left:
                    next_level.append((node.left, max_val))

                if node.right:
                    next_level.append((node.right, max_val))

            level = next_level

        return output

        # ==================== Method 1 - DFS 递归 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(n)，空间复杂度 O(h)（递归栈深度）
        # 递归定义：以 node 为根的子树中好节点个数
        #         = 当前节点是否是好节点（0 或 1）+ 左子树好节点数 + 右子树好节点数

        def dfs(node, max_val):
            """返回以 node 为根的子树中好节点个数，max_val 为根到 node 父节点路径上的最大值"""
            # 空节点没有好节点
            if node is None:
                return 0

            # 判断当前节点是否是好节点，是的话更新路径最大值
            good_node = 0
            if node.val >= max_val:
                good_node = 1
                max_val = node.val

            # 把更新后的最大值传给左右子树，分别统计
            # max_val 是参数（局部变量），左右分支各自拿到的是同一个值，互不干扰
            num_good_nodes = dfs(node.left, max_val) + dfs(node.right, max_val)

            return good_node + num_good_nodes

        # 根节点用自己的值作为初始最大值
        return dfs(root, root.val)