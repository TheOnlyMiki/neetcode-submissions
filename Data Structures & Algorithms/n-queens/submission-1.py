class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        题目：在 n × n 的棋盘上放 n 个皇后，使任意两个皇后不能互相攻击
             （不能在同一行、同一列、同一条斜线上），返回所有摆法。
        思路：回溯，逐行放皇后：
        - 每一行恰好放一个皇后 → 按行递归，第 row 层决定第 row 行的皇后放在哪一列，
          这样"同一行"的冲突天然不会发生
        - 列和两条斜线的冲突，用三个集合记录已被占用的位置，O(1) 判断
        斜线的表示方法（关键）：
        - 同一条"/"方向斜线上的格子，row + col 相同
          例：(0,2) (1,1) (2,0) → 都是 2
        - 同一条"\"方向斜线上的格子，row - col 相同
          例：(0,0) (1,1) (2,2) → 都是 0
        所以只要记录 row + col 和 row - col 是否出现过，就能判断斜线冲突。
        例：n = 4，两种解法
            [".Q..",      ["..Q.",
             "...Q",       "Q...",
             "Q...",       "...Q",
             "..Q."]       ".Q.."]
        时间复杂度 O(n!)：第一行 n 种选择，第二行最多 n - 1 种（列不能重复）……
                         实际因为斜线剪枝会更少；每个解生成棋盘需要 O(n²)
        空间复杂度 O(n)：三个集合、递归深度、path 都是 O(n)（不算输出）

        小提示：
        - 终止条件 len(path) == n 和 row == n 等价，因为每行恰好放一个。
        - row - col 可能为负数，用集合没问题；如果改用数组记录（更快），
          "\"斜线要加偏移量：下标为 row - col + n - 1，数组长度 2n - 1；
          "/"斜线下标 row + col，长度同样是 2n - 1。
        - 每行的字符串 '.' * col + 'Q' + '.' * (n - col - 1) 在放皇后时就生成好，
          到达叶子时直接复制 path 即可，不用再根据列号重建棋盘。
        - 位运算优化：用三个整数的二进制位代替三个集合，
          可用位置 = ~(cols | diag | anti_diag) & ((1 << n) - 1)，
          每次用 p & -p 取出最低位的 1 来放皇后，是 N 皇后最快的写法。
        - LeetCode 52（N 皇后 II）只要求返回解的个数，同样的回溯，把记录棋盘改成计数即可。
        """

        cols = set()           # 已被占用的列
        diag = set()           # 已被占用的"/"斜线（row + col）
        reverse_diag = set()   # 已被占用的"\"斜线（row - col）

        output = []   # 所有合法棋盘

        def dfs(row, path):
            """
            row ：当前要放皇后的行
            path：前 row 行的棋盘字符串（每行一个皇后）
            """
            # n 行都放好了皇后：得到一个合法棋盘（必须复制）
            if len(path) == n:
                output.append(path[:])
                return

            # 尝试把本行的皇后放在每一列
            for col in range(n):
                # 列冲突、"/"斜线冲突、"\"斜线冲突，任一成立就不能放
                if col in cols or row + col in diag or row - col in reverse_diag:
                    continue

                # 做选择：占用这一列和两条斜线
                cols.add(col)
                diag.add(row + col)
                reverse_diag.add(row - col)

                # 生成这一行的字符串：皇后在第 col 列
                path.append('.' * col + 'Q' + '.' * (n - col - 1))

                # 递归：处理下一行
                dfs(row+1, path)

                # 撤销选择：恢复棋盘和三个集合
                path.pop()

                cols.remove(col)
                diag.remove(row + col)
                reverse_diag.remove(row - col)

        dfs(0, [])

        return output