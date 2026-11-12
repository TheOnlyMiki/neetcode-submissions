# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    """
    题目：设计二叉树的序列化（树 → 字符串）与反序列化（字符串 → 树），
         要求反序列化后得到与原来完全相同的树。
    思路：前序遍历（根 → 左 → 右）序列化，并且记录空节点。
    为什么记录空节点就够了：
    - 只有前序序列无法唯一确定树（不知道哪里是叶子、子树在哪结束）
    - 记录空节点后，每个子树在序列中都以"恰好够数的空节点"结尾，结构信息就完整了，
      反序列化时按同样的前序顺序读，读到空标记就返回 None，不需要中序辅助
    符号约定：
    - "!" 表示空节点
    - "?" 是分隔符，防止多位数、负数之间粘连（如 1、23 和 12、3 区分不开）
    例：    1
           / \
          2   3
             / \
            4   5
        序列化结果："1?2?!?!?3?4?!?!?5?!?!"

    小提示：
    - 反序列化用 self.preorder_i 作为全局读指针，原理和 LeetCode 105（前序 + 中序建树）
      的前序指针一样：必须先建左子树再建右子树，指针才会按前序顺序正确往后走。
    - 读指针也可以换成迭代器，更简洁：
          vals = iter(data.split('?'))
          def dfs():
              val = next(vals)
              if val == '!':
                  return None
              node = TreeNode(int(val))
              node.left = dfs()
              node.right = dfs()
              return node
    - 递归深度等于树高，链状树最深可达节点数（本题最多 10^4），
      本地运行可能超过 Python 默认递归上限 1000，需要 sys.setrecursionlimit 或改用 BFS。
    - BFS（层序）序列化也是常见写法，LeetCode 自己展示树用的就是层序格式
      （如 [1,2,3,null,null,4,5]），面试时可以提一句。
    - 和 LeetCode 572（另一棵树的子树）的序列化写法同理，分隔符和空节点标记缺一不可。
    """

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        前序遍历序列化，空节点记为 "!"，各元素之间用 "?" 连接
        时间复杂度 O(n)，空间复杂度 O(n)
        """

        record = []   # 收集各节点的字符串，最后 join（比反复字符串拼接高效）

        def dfs(root):
            # 空节点也要记录，否则无法还原树的结构
            if root is None:
                record.append("!")
                return

            # 前序：先记录根
            record.append(str(root.val))

            # 再依次序列化左、右子树
            dfs(root.left)
            dfs(root.right)

            return

        dfs(root)

        # 用分隔符连接，例如 ["1", "2", "!", "!"] → "1?2?!?!"
        output = "?".join(record)

        return output

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        # ==================== Method 2 - split 后按前序顺序重建 ====================
        # 时间复杂度 O(n)，空间复杂度 O(n)
        # 思路：先按分隔符切成列表，然后用读指针按前序顺序依次取元素，
        #      序列化时怎么走的，反序列化就怎么走回来

        data = data.split('?')   # "1?2?!?!" → ["1", "2", "!", "!"]

        # 读指针：下一个要读取的元素下标
        self.preorder_i = 0

        def dfs():
            # 读到空标记：消耗这个元素，返回空节点
            if data[self.preorder_i] == '!':
                self.preorder_i += 1
                return None

            # 读到数字：创建当前子树的根
            node = TreeNode(int(data[self.preorder_i]))
            self.preorder_i += 1

            # 前序顺序：先建左子树，再建右子树
            # 左子树会消耗掉属于它的所有元素（包括空标记），之后指针正好指向右子树的开头
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

        # ==================== Method 1 - 不 split，直接在字符串上逐字符扫描 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(n)：每个字符只被扫描一次
        # 空间复杂度 O(h)：不额外生成列表，只有递归栈（int() 切片的临时字符串很短）
        # 此时 data 是原始字符串，self.preorder_i 是字符下标而不是元素下标

        self.preorder_i = 0

        def dfs():
            # 空标记 "!" 后面跟着一个分隔符 "?"，所以一次跳过 2 个字符
            # 序列最后一个元素一定是 "!"（最右叶子的右孩子），它后面没有 "?"，
            # 跳 2 会越过字符串末尾，但之后不会再读取，所以没有问题
            if data[self.preorder_i] == '!':
                self.preorder_i += 2
                return None

            # 向后扫描，找到当前数字的长度（直到遇到分隔符 "?"）
            # 数字后面一定还有元素（至少有它的两个空孩子），所以一定能遇到 "?"，不会越界
            length = 0
            while data[self.preorder_i + length] != '?':
                length += 1

            # 截取数字字符串并转成整数（支持多位数和负号）
            node = TreeNode(int(data[self.preorder_i : self.preorder_i + length]))

            # 跳过数字本身和后面的分隔符
            self.preorder_i += length + 1

            # 前序顺序：先建左子树，再建右子树
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()