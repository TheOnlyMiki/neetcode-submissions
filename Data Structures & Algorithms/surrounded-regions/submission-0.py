class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        题目：由 'X' 和 'O' 组成的网格，把所有被 'X' 完全包围的 'O' 区域都改成 'X'（原地修改）。
             与边界上的 'O' 相连（上下左右）的 'O' 不算被包围，保持不变。
        思路：反向思考，从边界出发（和 LeetCode 417 太平洋大西洋水流同一个思路）
        - 直接判断"哪些 'O' 被包围"很麻烦：要确认整片区域都碰不到边界
        - 反过来：不会被包围的 'O'，一定和边界上的某个 'O' 相连
          所以从四条边上的每个 'O' 出发 DFS，标记所有与边界相连的 'O'
        - 剩下没被标记的 'O' 就是被包围的，改成 'X'
        例：X X X X        X X X X
            X O O X   →    X X X X
            X X O X        X X X X
            X O X X        X O X X   （底边的 O 与边界相连，保留）
        时间复杂度 O(m · n)：每个 'O' 最多被加入集合一次，整个网格再遍历两遍
        空间复杂度 O(m · n)：集合 + 递归深度

        小提示：
        - 最后先全部改成 'X'，再把与边界相连的格子恢复成 'O'，
          等价于"未被标记的 'O' 改成 'X'"，写法很简洁。
        - 不用额外集合的原地写法：DFS 时把与边界相连的 'O' 临时改成 '#'，
          最后遍历一遍：'O' → 'X'（被包围），'#' → 'O'（恢复），额外空间只有递归栈。
        - 当前 dfs 对 'X' 格子不会加入 visit，所以同一个 'X' 可能被调用多次，
          但每次进入后立刻因为不是 'O' 而返回，只是 O(1) 的开销，不影响整体复杂度；
          也可以在调用前就判断 board[x][y] == 'O'，少一些函数调用。
        - 递归深度最坏为 m · n（本题最大 200 × 200），本地运行可能超出 Python 默认递归上限，
          可以改成多源 BFS：把边界上所有 'O' 一起入队。
        - 并查集也能做：把边界上的 'O' 都连到一个虚拟节点，最后不和虚拟节点连通的 'O' 改成 'X'。
        """

        m, n = len(board), len(board[0])

        def dfs(i, j, visit):
            """从 (i, j) 出发，把与它相连的所有 'O' 加入 visit"""
            # 只有 'O' 才继续扩展；'X' 直接返回
            if board[i][j] == 'O':
                visit.add((i, j))

                for a,b in [(1,0),(0,1),(-1,0),(0,-1)]:
                    x,y = i+a, j+b
                    # 不越界且还没访问过
                    if 0 <= x < m and 0 <= y < n and (x,y) not in visit:
                        dfs(x, y, visit)

        # 与边界相连的 'O'（不会被包围，最后要保留）
        cells_connect_edge = set()

        # ---------- 从左右两列的格子出发 ----------
        for i in range(m):
            dfs(i, 0, cells_connect_edge)
            dfs(i, n-1, cells_connect_edge)

        # ---------- 从上下两行的格子出发 ----------
        for j in range(n):
            dfs(0, j, cells_connect_edge)
            dfs(m-1, j, cells_connect_edge)

        # ---------- 先全部改成 'X'，再恢复与边界相连的 'O' ----------
        # 效果：被包围的 'O' 变成 'X'，其余保持原样
        for i in range(m):
            for j in range(n):
                board[i][j] = 'X'

        for i, j in cells_connect_edge:
            board[i][j] = 'O'

        return