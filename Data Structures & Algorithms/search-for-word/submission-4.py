class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        题目：在 m × n 的字符网格中，判断能否找到单词 word。
             单词由相邻（上下左右）格子的字母按顺序组成，同一个格子不能重复使用。
        思路：回溯（DFS）
        - 枚举每个格子作为起点
        - 从起点出发，当前格子匹配 word[word_i] 就继续往四个方向找 word[word_i + 1]
        - 一条路径上走过的格子要标记为"已使用"，回溯时再撤销标记
        三种方法只在"如何标记已使用的格子"上不同：
        - Method 3：直接把 board 上的字符改成 '.'，回溯时改回来（不需要额外空间）
        - Method 2：额外的 visited 二维数组
        - Method 1：哈希集合 path 存走过的坐标
        时间复杂度 O(m · n · 3^L)：L 为单词长度，每个起点出发，
                                 除第一步有 4 个方向外，之后每步最多 3 个方向（不能走回头路）
        空间复杂度：递归深度 O(L)；Method 2 额外 O(m · n)，Method 1 额外 O(L)

        小提示：
        - Method 3 找到答案后直接 return True，没有把 board 改回来，
          网格会残留 '.'。LeetCode 不检查这一点，但如果题目要求不能修改输入，
          应该先保存结果、恢复 board[i][j] 后再返回（像 Method 2 那样用 res 变量）。
        - 改成 '.' 能当作"已访问"标记，前提是 word 中不会出现 '.'
          （题目保证只有英文字母），否则要换成别的特殊字符，如 '#'。
        - 三个方向的 or 会短路：只要某个方向找到了就不再尝试其他方向。
        - 常见剪枝（面试追问"如何优化"）：
          · 先统计 board 和 word 的字符频率，word 中某个字母的数量多于 board 中的，直接返回 False
          · 如果 word 首字母在 board 中出现次数比尾字母多，就把 word 反转后再搜，
            起点更少，搜索树更小
        - 进阶题 LeetCode 212（单词搜索 II）：一次查找多个单词，
          需要把所有单词建成 Trie（前缀树），一边 DFS 一边在 Trie 上往下走。
        """

        # ==================== Method 3 - 回溯，直接修改 board 做标记 ====================
        # 额外空间只有递归栈 O(L)

        m, n = len(board), len(board[0])

        def backtrack(i, j, word_i):
            """
            从格子 (i, j) 开始，判断能否匹配 word[word_i:]
            """
            # word 的所有字母都已匹配完
            # （放在越界判断之前：最后一个字母匹配后，下一层可能越界，但已经成功了）
            if word_i == len(word):
                return True

            # 越界，或当前格子字母不匹配（已访问的格子是 '.'，也一定不匹配）
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[word_i]:
                return False

            # 做选择：标记当前格子已使用，避免同一路径重复使用
            board[i][j] = '.'

            # 往上、左、下、右四个方向继续匹配下一个字母，任意一个成功即可
            if (backtrack(i-1, j, word_i+1) or
                backtrack(i, j-1, word_i+1) or
                backtrack(i+1, j, word_i+1) or
                backtrack(i, j+1, word_i+1)):
                return True

            # 撤销选择：四个方向都失败，恢复格子原本的字母（就是 word[word_i]）
            board[i][j] = word[word_i]

            return False

        # 枚举每个格子作为起点
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False

        # ==================== Method 2 - 回溯，visited 数组做标记 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 额外空间 O(m · n)：visited 数组；不修改 board

        ROWS, COLS = len(board), len(board[0])

        # visited[r][c] 为 True 表示 (r, c) 已在当前路径上
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, i):
            # 全部字母匹配完
            if i == len(word):
                return True

            # 越界、字母不匹配、或已在当前路径上
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or visited[r][c]):
                return False

            visited[r][c] = True   # 做选择

            # 四个方向继续搜索，结果先存下来
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            # 撤销选择：无论成功失败都恢复，保证状态干净
            visited[r][c] = False
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

        # ==================== Method 1 - 回溯，哈希集合做标记 ====================
        # 额外空间 O(L)：集合中最多存当前路径上的 L 个坐标；
        # 但每次查询、插入都要计算元组哈希，常数比数组大

        ROWS, COLS = len(board), len(board[0])

        # 当前路径上已使用的坐标
        path = set()

        def dfs(r, c, i):
            # 全部字母匹配完
            if i == len(word):
                return True

            # 越界（min(r, c) < 0 同时检查行列是否为负）、字母不匹配、或已在路径上
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            path.add((r, c))   # 做选择

            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            path.remove((r, c))   # 撤销选择
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False