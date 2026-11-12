class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        length = len(endWord)

        pattern_2_word = defaultdict(list)
        word_2_pattern = {}

        word_set.add(beginWord)

        for word in word_set:
            pattern = []
            for i in range(length):
                key = word[:i] + '.' + word[i+1:]
                pattern_2_word[key].append(word)
                pattern.append(key)
            word_2_pattern[word] = pattern

        front_tree_level = {beginWord}
        back_tree_level = {endWord}   # 小提示：两边的前沿都用 set，因为"邻居在不在对面"要 O(1) 判断
        visited = {beginWord, endWord}          # 小提示：两边共用一个 visited，一个词被任意一边占了，另一边就不会再走它

        step = 1   # 小提示：step 表示"路径上的单词数"。初始只有 beginWord，第一轮若直接和 endWord 相遇，路径是 [begin, end]，step 变成 2，正好

        while front_tree_level and back_tree_level:
            if len(front_tree_level) > len(back_tree_level):
                front_tree_level, back_tree_level = back_tree_level, front_tree_level   # 小提示：永远扩展较小的一边；交换之后下面的代码不用区分是哪一边，写起来最简单

            step += 1
            next_level = set()

            for word in front_tree_level:
                for pattern in word_2_pattern[word]:
                    for next_word in pattern_2_word[pattern]:
                        if next_word in back_tree_level:   # 小提示：相遇判断必须放在 visited 判断之前，因为对面的词已经在 visited 里了，顺序反了就永远遇不上
                            return step

                        if next_word not in visited:
                            visited.add(next_word)
                            next_level.add(next_word)
                    # 小提示：这里故意不删桶。一个桶被这一边扫掉之后，对面可能要靠同一个桶判断相遇。双向 BFS 本身已经把搜索量降成 2·b^(d/2)，删桶的收益不大，不值得冒这个风险

            front_tree_level = next_level

        return 0   # 小提示：任意一边前沿变空，说明那一边能走到的词都走完了还没相遇，两边不连通

        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        length = len(endWord)
        
        pattern_2_word = defaultdict(list)
        word_2_pattern = {}

        word_set.add(beginWord)

        for word in word_set:
            pattern = []

            for i in range(length):
                key = word[:i] + '.' + word[i+1:]
                pattern_2_word[key].append(word)
                pattern.append(key)

            word_2_pattern[word] = pattern

        level = [beginWord]

        visit_words = {beginWord}

        step = 0

        while level:
            next_level = []
            step += 1

            for word in level:
                    for pattern in word_2_pattern[word]:
                        for next_word in pattern_2_word[pattern]:
                            if next_word == endWord:
                                return step + 1

                            if next_word not in visit_words:
                                visit_words.add(next_word)
                                next_level.append(next_word)

                        del pattern_2_word[pattern]

            level = next_level

        return 0

