class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        题目：单词接龙。从 beginWord 变到 endWord，每次只能改一个字母，
             且每个中间单词都必须在 wordList 中。返回最短转换序列中的单词数；无法转换返回 0。
        思路：把每个单词看成图中的节点，只差一个字母的两个单词之间连边，
             求 beginWord 到 endWord 的最短路径 → 无权图最短路 → BFS
        建图技巧（通配符分桶）：
        - 对每个单词，把第 i 位换成 '.' 得到 L 个"模式"，如 "hot" → ".ot"、"h.t"、"ho."
        - 落在同一个模式桶里的单词，彼此只差一个字母，互为邻居
        - pattern_2_word：模式 → 属于这个模式的所有单词
        - word_2_pattern：单词 → 它的所有模式（BFS 时用来找邻居桶）
        这样找邻居不需要两两比较所有单词。
        例：beginWord = "hit"，endWord = "cog"，
            wordList = ["hot","dot","dog","lot","log","cog"]
            hit → hot → dot → dog → cog，共 5 个单词 → 返回 5
        复杂度（N 为单词数，L 为单词长度）：
        - 建桶：O(N · L²)，每个单词生成 L 个模式，每个模式切片拼接 O(L)
        - BFS：O(N · L²)，每个单词出队一次，遍历它的 L 个桶
        - 空间：O(N · L²)，所有模式字符串

        小提示：
        - Method 2（双向 BFS）：
          · 两边的前沿都用 set，因为"邻居在不在对面"要 O(1) 判断。
          · 两边共用一个 visited，一个词被任意一边占了，另一边就不会再走它。
          · step 表示"路径上的单词数"。初始只有 beginWord，第一轮若直接和 endWord 相遇，
            路径是 [begin, end]，step 变成 2，正好。
          · 永远扩展较小的一边；交换之后下面的代码不用区分是哪一边，写起来最简单。
          · 相遇判断必须放在 visited 判断之前，因为对面的词已经在 visited 里了，顺序反了就永远遇不上。
          · 这里故意不删桶。一个桶被这一边扫掉之后，对面可能要靠同一个桶判断相遇。
            双向 BFS 本身已经把搜索量降成 2·b^(d/2)，删桶的收益不大，不值得冒这个风险。
          · 任意一边前沿变空，说明那一边能走到的词都走完了还没相遇，两边不连通，返回 0。
        - Method 1（单向 BFS）扫完一个桶就 del：桶里的单词这时都已经被访问过，
          以后再扫这个桶只会白跑。之后同一层另一个单词再访问这个模式时，
          defaultdict 会返回一个新的空列表，不会报错（如果用普通 dict 就要改成 .get(pattern, [])）。
        - endWord 不在 wordList 中直接返回 0；beginWord 不要求在 wordList 中，所以要手动加入建桶。
        - 不分桶的写法：对每个单词的每一位尝试换成 'a'~'z'，查是否在 word_set 中，
          复杂度 O(N · L · 26 · L)，L 小时也可以接受。
        - 进阶题 LeetCode 126（单词接龙 II）要求输出所有最短路径：
          BFS 时记录每个单词的所有"上一层父节点"，再从 endWord 回溯 DFS 构造路径。
        """

        # ==================== Method 2 - 双向 BFS ====================

        word_set = set(wordList)

        # 终点不在字典中，不可能到达
        if endWord not in word_set:
            return 0

        length = len(endWord)

        pattern_2_word = defaultdict(list)   # 模式 → 单词列表
        word_2_pattern = {}                  # 单词 → 模式列表

        # 起点也要参与建桶，才能找到它的邻居
        word_set.add(beginWord)

        # ---------- 第 1 步：通配符分桶建图 ----------
        for word in word_set:
            pattern = []
            for i in range(length):
                key = word[:i] + '.' + word[i+1:]   # 第 i 位换成通配符
                pattern_2_word[key].append(word)
                pattern.append(key)
            word_2_pattern[word] = pattern

        # ---------- 第 2 步：从两端同时 BFS ----------
        front_tree_level = {beginWord}   # 一边的当前前沿
        back_tree_level = {endWord}      # 另一边的当前前沿
        visited = {beginWord, endWord}   # 两边共用

        step = 1   # 路径上的单词数

        while front_tree_level and back_tree_level:
            # 总是扩展较小的那一边，交换后统一处理 front
            if len(front_tree_level) > len(back_tree_level):
                front_tree_level, back_tree_level = back_tree_level, front_tree_level

            step += 1
            next_level = set()

            for word in front_tree_level:
                # 遍历当前单词所在的每个桶，桶里的单词都是它的邻居
                for pattern in word_2_pattern[word]:
                    for next_word in pattern_2_word[pattern]:
                        # 邻居已经在对面的前沿里：两边相遇，找到最短路径
                        if next_word in back_tree_level:
                            return step

                        # 新单词：标记访问，加入下一层
                        if next_word not in visited:
                            visited.add(next_word)
                            next_level.add(next_word)

            front_tree_level = next_level

        # 有一边走完了也没相遇，两端不连通
        return 0

        # ==================== Method 1 - 单向 BFS ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留

        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        length = len(endWord)

        pattern_2_word = defaultdict(list)
        word_2_pattern = {}

        word_set.add(beginWord)

        # ---------- 第 1 步：通配符分桶建图 ----------
        for word in word_set:
            pattern = []

            for i in range(length):
                key = word[:i] + '.' + word[i+1:]
                pattern_2_word[key].append(word)
                pattern.append(key)

            word_2_pattern[word] = pattern

        # ---------- 第 2 步：从 beginWord 开始逐层 BFS ----------
        level = [beginWord]

        visit_words = {beginWord}

        step = 1   # 当前层对应的路径单词数

        while level:
            next_level = []
            step += 1   # 下一层的单词在路径中是第 step 个

            for word in level:
                for pattern in word_2_pattern[word]:
                    for next_word in pattern_2_word[pattern]:
                        # 到达终点：BFS 第一次到达就是最短路径
                        if next_word == endWord:
                            return step

                        if next_word not in visit_words:
                            visit_words.add(next_word)
                            next_level.append(next_word)

                    # 这个桶里的单词都已访问，删掉避免以后重复扫描
                    del pattern_2_word[pattern]

            level = next_level

        # 所有能到达的单词都走完了也没遇到终点
        return 0