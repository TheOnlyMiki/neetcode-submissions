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
                if word == endWord:
                    return step

                if word not in visit_words:
                    visit_words.add(word)

                    for key in word_2_pattern[word]:
                        next_level += pattern_2_word[key]

            level = next_level

        return 0