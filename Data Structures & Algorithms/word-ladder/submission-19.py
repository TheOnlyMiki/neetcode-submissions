class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        word_set.add(beginWord)
        
        n = len(endWord)

        pattern2word = defaultdict(list)
        word2pattern = {}

        for word in word_set:
            pattern = []
            for i in range(n):
                key = word[:i] + '.' + word[i+1:]
                pattern2word[key].append(word)
                pattern.append(key)
            word2pattern[word] = pattern

        first_tree_level = {beginWord}
        back_tree_level = {endWord}

        visit = set()

        step = 1

        while first_tree_level and back_tree_level:
            if len(first_tree_level) < len(back_tree_level):
                first_tree_level, back_tree_level = back_tree_level, first_tree_level

            next_level = set()
            step += 1

            for word in first_tree_level:
                visit.add(word)

                for pattern in word2pattern[word]:
                    for next_word in pattern2word[pattern]:
                        if next_word in back_tree_level:
                            return step

                        if next_word not in visit:
                            next_level.add(next_word)

            first_tree_level = next_level

        return 0

            
