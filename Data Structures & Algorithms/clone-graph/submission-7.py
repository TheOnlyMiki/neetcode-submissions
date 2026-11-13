"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        copy = {}

        def dfs(current):
            if current in copy:
                return copy[current]

            copy[current] = Node(val=current.val)
            
            for next_node in current.neighbors:
                copy[current].neighbors.append(dfs(next_node))

            return copy[current]


        return dfs(node)



































        """
        题目：给定无向连通图中一个节点的引用，返回整张图的深拷贝。
             每个节点有值 val 和邻居列表 neighbors。
        思路：遍历原图 + 哈希表记录"原节点 → 新节点"的对应关系
        - 第一次遇到一个原节点时，立刻创建它的拷贝并登记到哈希表
        - 之后再遇到它（图中有环，会被多次遇到），直接从哈希表取出已有的拷贝
        - "在哈希表中"就等价于"已访问"，不需要额外的 visit 集合
        三种方法只是遍历方式不同：
        - Method 3：BFS 按层遍历
        - Method 2：DFS，在调用方登记，dfs 只负责连接邻居
        - Method 1：DFS，在被调用方登记，dfs 返回拷贝节点
        例：1 —— 2
            |    |
            4 —— 3
            每个节点只克隆一次，每个拷贝的 neighbors 和原节点一一对应
        时间复杂度 O(V + E)：每个节点克隆一次，每条边被两端各处理一次
        空间复杂度 O(V)：哈希表 + 队列 / 递归深度

        小提示：
        - 用原节点对象作为 key，而不是 node.val：不依赖"值互不相同"这个前提，
          即使图中有重复的值也能正确克隆。Node 没有重写 __hash__ / __eq__，
          默认按对象身份哈希，正好区分每个不同的节点。
        - "先登记再递归 / 入队"是三种写法共同的关键：
          如果等邻居都处理完才放进哈希表，遇到环 A → B → A 时 A 还不在表里，
          会再克隆一次 A（DFS 陷入无限递归，BFS 重复入队）。
        - 无论邻居是否已经克隆过，都要把它的拷贝加入当前拷贝的 neighbors：
          "是否已克隆"只决定要不要新建、要不要继续遍历，不影响连边。
          三种写法里 append 都放在 if 外面，正是这个原因。
        - BFS 没有递归，不受 Python 递归深度限制；本题最多 100 个节点，DFS 也没问题。
        - 和 LeetCode 138（复制带随机指针的链表）是同一个思路：哈希表存"旧 → 新"映射，
          解决"要指向的节点可能还没被复制"的问题。
        """

        # ==================== Method 3 - BFS ====================

        # 空图
        if not node:
            return None

        # 原节点 → 拷贝节点；起点先克隆并登记
        maps = {
            node : Node(val=node.val)
        }

        # 当前层的原节点（这些节点的拷贝都已创建，等待连接邻居）
        level = [node]

        while level:
            next_level = []

            for current in level:
                for next_node in current.neighbors:
                    # 邻居第一次遇到：克隆、登记，并放入下一层继续遍历
                    if next_node not in maps:
                        maps[next_node] = Node(val=next_node.val)
                        next_level.append(next_node)

                    # 无论是否新克隆，都要在拷贝之间建立同样的邻接关系
                    maps[current].neighbors.append(maps[next_node])

            level = next_level

        # 返回起点的拷贝
        return maps[node]

        # ==================== Method 2 - DFS（调用方登记） ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留

        if not node:
            return None

        # 原节点 → 拷贝节点；起点先克隆并登记
        maps = {
            node : Node(val=node.val)
        }

        def dfs(node):
            """
            调用前 node 的拷贝已经在 maps 中；
            负责把 node 拷贝的 neighbors 连好，并递归处理没克隆过的邻居
            """
            for next_node in node.neighbors:
                # 邻居第一次遇到：先克隆并登记，再递归处理它
                # 先登记保证递归中再遇到它时不会重复克隆
                if next_node not in maps:
                    maps[next_node] = Node(val=next_node.val)

                    dfs(next_node)

                # 无论是否新克隆，都连上邻接关系
                maps[node].neighbors.append(maps[next_node])

        dfs(node)

        return maps[node]

        # ==================== Method 1 - DFS（被调用方登记，返回拷贝） ====================

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