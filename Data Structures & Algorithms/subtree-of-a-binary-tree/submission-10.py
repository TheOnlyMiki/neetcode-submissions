# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        题目：判断 subRoot 是否是 root 的某个子树。
             子树 = root 中某个节点及其"全部"后代，必须完全一致（不能只匹配一部分）。
        """

        # ==================== Method 2 - 序列化 + 字符串匹配 ====================
        # 时间复杂度：序列化 O(m + n)；`in` 子串查找平均接近线性，
        #           若要严格保证 O(m + n) 可改用 KMP
        # 空间复杂度 O(m + n)：两个序列化字符串 + 递归栈
        # 思路：把两棵树都用前序遍历序列化成字符串，
        #      如果 subRoot 是 root 的子树，它的序列一定是 root 序列中连续的一段

        # 空树是任何树的子树
        if subRoot is None:
            return True

        # root 为空而 subRoot 不空，不可能匹配
        if root is None:
            return False

        res = []   # 收集序列化的各个片段，最后 join（比反复字符串拼接高效）

        def dfs(node):
            """前序遍历序列化：每个节点写成 "$值"，空节点写成 "$#" """
            # 空节点也必须记录，否则不同结构的树可能得到相同序列
            # 例：只有左孩子 2 的节点 1 和只有右孩子 2 的节点 1，不记空节点都是 "1,2"
            if node is None:
                res.append("$#")
                return

            # 每个值前加分隔符 "$"，防止数字粘连造成误匹配
            # 例：root 中有节点 12，subRoot 只有节点 2
            #     不加分隔符："12##" 包含 "2##" → 误判为子树
            #     加分隔符："$12$#$#" 不包含 "$2$#$#" → 正确
            # 值的结尾也有边界：后面一定紧跟下一个 "$"，所以 "$1" 不会匹配到 "$12" 的开头
            res.append("$")
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        # 序列化 root
        dfs(root)
        root_sentence = "".join(res)

        # 清空 res，复用 dfs 序列化 subRoot
        # （dfs 闭包引用的是变量名 res，重新赋值后它会写进新列表）
        res = []
        dfs(subRoot)
        subRoot_sentence = "".join(res)

        # subRoot 的序列是 root 序列的子串 ⇔ subRoot 是 root 的子树
        return subRoot_sentence in root_sentence

        # ==================== Method 1 - 遍历 root 的每个节点，逐个判断是否相同 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(m × n)：root 的每个节点都可能和 subRoot 完整比较一次
        # 空间复杂度 O(w)：BFS 队列宽度
        # 思路：BFS 遍历 root，把每个节点都当作候选子树的根，用 isSameTree 判断

        # 空树是任何树的子树
        if subRoot is None:
            return True

        # root 为空而 subRoot 不空，不可能匹配
        if root is None:
            return False

        def isSameTree(p, q):
            """判断两棵树是否完全相同（即 LeetCode 100，BFS 写法）"""
            # 当前层的"对应位置节点对"
            level = [(p, q)]

            while level:
                next_level = []

                for (p_node, q_node) in level:
                    # 都为空：这一位置相同
                    if p_node is None and q_node is None:
                        continue

                    # 一个空一个不空，或值不同
                    if p_node is None or q_node is None or q_node.val != p_node.val:
                        return False

                    # 当前一对相同，继续比较左孩子对、右孩子对
                    next_level += [(p_node.left, q_node.left), (p_node.right, q_node.right)]

                level = next_level

            return True

        # BFS 遍历 root 的所有节点
        level = [root]

        while level:
            next_level = []

            for node in level:
                # 以当前节点为根的子树和 subRoot 相同，找到了
                # （node 为 None 时 isSameTree 也会直接返回 False，因为 subRoot 非空）
                if isSameTree(node, subRoot):
                    return True

                if node:
                    next_level += [node.left, node.right]

            level = next_level

        return False