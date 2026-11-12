# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        题目：根据前序遍历和中序遍历结果，还原二叉树（节点值互不相同）。
        关键性质：
        - 前序（根 → 左 → 右）：第一个元素一定是根
        - 中序（左 → 根 → 右）：根的左边全是左子树，右边全是右子树
        所以：用前序确定根，再到中序里找根的位置，就能把树切成左右两半，递归构建。
        例：preorder = [3, 9, 20, 15, 7]，inorder = [9, 3, 15, 20, 7]
            根是 3；中序里 3 的左边 [9] 是左子树，右边 [15, 20, 7] 是右子树
                3
               / \
              9  20
                 / \
                15  7

        小提示：
        - Method 2 里"先建左子树再建右子树"是这个写法成立的前提，面试最常被问到。
        - 如果换成"中序 + 后序"（LeetCode 106）：后序是"左 → 右 → 根"，
          根在最后，要让指针从后往前走，并且先建右子树再建左子树。
        - "前序 + 后序"不能唯一确定一棵二叉树（只有一个孩子时分不清是左还是右），
          所以构造题一定需要中序参与。LeetCode 889 是前序 + 后序的特例，
          只要求返回任意一个合法结果。
        """

        # ==================== Method 2 - 哈希表 + 全局前序指针 ====================
        # 时间复杂度 O(n)：每个节点只创建一次，哈希表 O(1) 找根的位置
        # 空间复杂度 O(n)：哈希表 O(n)，递归栈 O(h)
        # 思路：不切片，用下标区间 [l, r] 表示中序里当前子树的范围；
        #      前序则用一个全局指针按顺序依次取根

        # 值 → 在中序中的下标，O(1) 找到根的位置（代替 inorder.index 的 O(n) 查找）
        inorder_i = {val: i for i, val in enumerate(inorder)}

        # 前序指针：下一个要用作根的元素在 preorder 中的下标
        # 用 self 属性是为了让嵌套函数能修改它（也可以用 nonlocal）
        self.preorder_i = 0

        def dfs(l, r):
            """用中序区间 inorder[l..r] 内的节点构建子树，返回子树的根"""
            # 区间为空，没有节点
            if l > r:
                return None

            # 前序的下一个元素就是当前子树的根
            root = preorder[self.preorder_i]
            self.preorder_i += 1

            # 根在中序中的位置，把区间分成左右两部分
            mid = inorder_i[root]

            root = TreeNode(val=root)

            # 必须先建左子树再建右子树！
            # 因为前序是"根 → 左 → 右"，preorder_i 按这个顺序往后走：
            # 建完根之后，接下来的若干个元素都属于左子树，用完了才轮到右子树
            root.left = dfs(l, mid-1)    # 中序中根左边的部分
            root.right = dfs(mid+1, r)   # 中序中根右边的部分

            return root

        return dfs(0, len(preorder)-1)

        # ==================== Method 1 - 数组切片递归 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(n²)：每层 inorder.index 是 O(n)，切片也是 O(n)，最坏（链状树）有 n 层
        # 空间复杂度 O(n²)：每层切片都会复制出新列表
        # 思路最直观：直接把两个数组切成左右子树对应的部分，递归构建

        def dfs(preorder, inorder):
            # 没有节点了
            if not preorder or not inorder:
                return None

            # 前序第一个元素是根
            root = preorder[0]

            # 根在中序中的下标，同时也等于左子树的节点个数
            mid = inorder.index(root)

            root = TreeNode(val=root)

            # 左子树有 mid 个节点：
            # - 前序中紧跟在根后面的 mid 个元素：preorder[1 : mid+1]
            # - 中序中根左边的部分：inorder[:mid]
            root.left = dfs(preorder[1:mid+1], inorder[:mid])

            # 右子树是剩下的部分：
            # - 前序中左子树之后的所有元素：preorder[mid+1:]
            # - 中序中根右边的部分：inorder[mid+1:]
            root.right = dfs(preorder[mid+1:], inorder[mid+1:])

            return root

        return dfs(preorder, inorder)