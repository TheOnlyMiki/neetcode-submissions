"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        题目：给定无向连通图中一个节点的引用，返回整张图的深拷贝。
             每个节点有值 val 和邻居列表 neighbors。
        思路：DFS + 哈希表记录"原节点 → 新节点"的对应关系
        - 进入一个原节点时，先创建它的拷贝并登记到 record，再递归处理它的邻居
        - 如果某个原节点已经在 record 中，说明已经克隆过（或正在克隆），直接返回它的拷贝
        - "在 record 中"就等价于"已访问"，不需要额外的 visit 集合
        例：1 —— 2
            |    |
            4 —— 3
            dfs(1)：克隆 1 并登记 → 递归邻居 2
              dfs(2)：克隆 2 并登记 → 邻居 1 已在 record，直接返回拷贝 → 递归邻居 3
                dfs(3)：克隆 3 并登记 → 邻居 2 已登记 → 递归邻居 4
                  dfs(4)：克隆 4 并登记 → 邻居 1、3 都已登记
            每个节点只克隆一次，环不会导致无限递归
        时间复杂度 O(V + E)：每个节点克隆一次，每条边被两端各处理一次
        空间复杂度 O(V)：哈希表和递归深度

        小提示：
        - 用原节点对象作为 key，而不是 node.val：不依赖"值互不相同"这个前提，
          即使图中有重复的值也能正确克隆。Node 没有重写 __hash__ / __eq__，
          默认按对象身份哈希，正好区分每个不同的节点。
        - "先登记再递归"是关键：如果等邻居都克隆完才放进 record，
          遇到环 A → B → A 时 A 还不在表里，会再克隆一次 A，陷入无限递归。
          先登记后，即使 A 的邻居还没处理完，再遇到 A 也能直接拿到它的拷贝。
        - dfs 返回拷贝节点，调用方直接 append 返回值，邻接关系的建立变得很简洁。
        - BFS 写法同理：先克隆起点入队，出队时遍历邻居，
          邻居不在 record 中就克隆、登记并入队，然后把邻居拷贝加入当前拷贝的 neighbors。
        - 和 LeetCode 138（复制带随机指针的链表）是同一个思路：哈希表存"旧 → 新"映射，
          解决"要指向的节点可能还没被复制"的问题。
        """

        # 空图
        if not node:
            return None

        # 原节点 → 拷贝节点
        record = {}

        def dfs(node):
            """返回原节点 node 对应的拷贝节点（会递归克隆它能到达的整张图）"""
            # 已经克隆过（或正在克隆中，处于环上），直接返回已有的拷贝
            if node in record:
                return record[node]

            # 先创建拷贝并登记，再处理邻居
            copy = Node(val=node.val)
            record[node] = copy

            # 递归克隆每个邻居，并把邻居的拷贝加入当前拷贝的邻居列表
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)