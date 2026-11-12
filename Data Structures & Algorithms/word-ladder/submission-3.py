class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        visit_words = set(wordList)

        if endWord not in visit_words:
            return 0

        length = len(endWord)
        
        pattern_2_word = defaultdict(list)
        word_2_pattern = defaultdict(list)

        for word in visit_words:
            pattern = []

            for i in range(length):
                key = word[:i] + '.' + word[i+1:]
                pattern_2_word[key].append(word)
                pattern.append(key)

            word_2_pattern[word] = pattern

        pattern = []
        for i in range(length):
            key = beginWord[:i] + '.' + beginWord[i+1:]
            pattern_2_word[key].append(beginWord)
            pattern.append(key)
        word_2_pattern[beginWord] = pattern
        
        level = [beginWord]

        visit_words = set()

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

            level = next_level

        return 0