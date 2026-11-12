class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        m, n = len(board), len(board[0])

        tree_head = {}

        def prefixTreeInsert(word):
            node = tree_head
            for c in word:
                if c not in node:
                    node[c] = {}

                node = node[c]

            node['#'] = word

        for word in words:
            prefixTreeInsert(word)

        output = []

        def dfs(node, i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] in node:

                c = board[i][j]
                board[i][j] = '.'

                word = node[c].pop('#', False)
                if word:
                    output.append(word)

                for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    dfs(node[c], i+a, j+b)

                board[i][j] = c

                if not node[c]:
                    del node[c]

            return

        for i in range(m):
            for j in range(n):
                dfs(tree_head, i, j)

        return output
















        """
        题目：给定 m × n 字符网格和单词列表 words，找出所有能在网格中找到的单词。
             单词由相邻（上下左右）格子按顺序组成，同一单词中同一格子不能重复使用。
        思路：前缀树（Trie）+ 网格回溯
        - 朴素做法：对每个单词都跑一遍 LeetCode 79（单词搜索），单词多时会超时
        - 改进：把所有单词建成一棵 Trie，网格 DFS 时同步在 Trie 上往下走：
          · 当前格子的字母不在 Trie 当前节点的孩子里 → 没有任何单词以这条路径为前缀，立刻剪枝
          · 走到 Trie 中某个单词的结尾 → 找到一个单词
          这样一次 DFS 就同时搜索了所有共享该前缀的单词
        Trie 用嵌套字典实现：
        - node[c] 是字符 c 对应的子节点（也是一个字典）
        - node['#'] = word 表示从根到这里构成完整单词 word（直接存单词本身，找到时不用再拼路径）
        例：words = ["oath", "oat", "eat"]
            tree_head = {'o': {'a': {'t': {'#': 'oat', 'h': {'#': 'oath'}}}},
                         'e': {'a': {'t': {'#': 'eat'}}}}
        复杂度（L 为最长单词长度，S 为所有单词总长度）：
        - 建树：O(S)
        - 搜索：最坏 O(m · n · 4 · 3^(L-1))，每个起点第一步 4 个方向，之后每步最多 3 个
        - 空间：Trie O(S)，递归深度 O(L)

        小提示：
        - 两个关键优化，缺一个都可能超时：
          · 找到单词后 pop('#')：同一个单词可能在网格里有多条路径，pop 后不会重复加入结果，
            也就不需要用 set 去重
          · 回溯结束后若 node[c] 已经为空就 del：这个分支下的单词都已经找到了，
            把整条分支从 Trie 上剪掉，之后的 DFS 一进来就会被"不在 node 中"挡住
        - '.' 用来标记"当前路径已使用"的格子，因为 Trie 里不会有 '.' 这个 key，
          所以 board[i][j] in node 的判断自动把已访问的格子排除掉了。
        - '#' 作为单词结尾标记，前提是单词中不会出现 '#'（题目保证只有小写字母）。
        - 两种写法的区别只在边界检查的位置：
          · Method 2：先递归，进入后再检查越界和字母（写法更短，但多一些无效调用）
          · Method 1：调用前先检查越界和是否访问过（少一些函数调用，稍快）
        - 和 LeetCode 79 对比：79 只找一个单词，用 word_i 下标记录进度；
          212 找多个单词，用 Trie 节点记录进度，本质是一样的回溯。
        """

        # ==================== Method 2 - 进入后再检查边界 ====================

        # ---------- 第 1 步：用所有单词建立前缀树 ----------
        tree_head = {}

        def prefixTreeInsert(node, word):
            # 沿单词字符往下走，没有的边就新建一个空字典
            for c in word:
                if c not in node:
                    node[c] = {}

                node = node[c]

            # 在单词结尾节点存下单词本身
            node['#'] = word

        for word in words:
            prefixTreeInsert(tree_head, word)

        m, n = len(board), len(board[0])

        # ---------- 第 2 步：网格 DFS，同步在前缀树上往下走 ----------
        def dfs(i, j, node):
            """
            (i, j)：当前格子
            node  ：前缀树中当前所在的节点（已匹配完之前路径上的字母）
            """
            # 不越界，且当前格子的字母是 node 的孩子（即存在以当前路径为前缀的单词）
            # 已访问的格子是 '.'，不会在 node 中，所以这里也排除了走回头路
            if 0 <= i < m and 0 <= j < n and board[i][j] in node:
                c = board[i][j]

                # 做选择：标记当前格子已使用
                board[i][j] = '.'

                # 走到某个单词的结尾：加入结果，并 pop 掉标记避免重复加入
                if '#' in node[c]:
                    output.append(node[c].pop('#'))

                # 四个方向继续匹配下一个字母
                for a, b in [(1,0), (0, 1), (-1, 0), (0, -1)]:
                    dfs(i+a, j+b, node[c])

                # 撤销选择：恢复格子原本的字母
                board[i][j] = c

                # 剪枝：这个分支下的单词都已找到（子节点为空），从前缀树上删除
                if not node[c]:
                    del node[c]

        output = []

        # 枚举每个格子作为起点
        for i in range(m):
            for j in range(n):
                dfs(i, j, tree_head)

        return output

        # ==================== Method 1 - 调用前先检查边界 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留

        # ---------- 第 1 步：用所有单词建立前缀树 ----------
        tree_head = {}

        def prefixTreeInsert(node, word):
            for c in word:
                if c not in node:
                    node[c] = {}

                node = node[c]

            node['#'] = word

        for word in words:
            prefixTreeInsert(tree_head, word)

        m, n = len(board), len(board[0])

        # ---------- 第 2 步：网格 DFS ----------
        def dfs(i, j, node):
            """调用方保证 (i, j) 不越界且未被访问"""
            # 当前字母不在前缀树中：没有单词以当前路径为前缀，剪枝
            # （起点调用时没有预先检查，所以这里仍需判断）
            if board[i][j] not in node:
                return

            c = board[i][j]

            # 取出并删除单词结尾标记；没有则返回 False
            isWord = node[c].pop('#', False)

            if isWord:
                output.append(isWord)

            # 做选择：标记当前格子已使用
            board[i][j] = '.'

            # 先检查越界和是否已访问，再递归，减少无效的函数调用
            for a, b in [(1,0), (0, 1), (-1, 0), (0, -1)]:
                next_i, next_j = i+a, j+b
                if 0 <= next_i < m and 0 <= next_j < n and board[next_i][next_j] != '.':
                    dfs(next_i, next_j, node[c])

            # 撤销选择
            board[i][j] = c

            # 剪枝：分支下的单词都已找到，从前缀树上删除
            if not node[c]:
                del node[c]

            return

        output = []

        for i in range(m):
            for j in range(n):
                dfs(i, j, tree_head)

        return output