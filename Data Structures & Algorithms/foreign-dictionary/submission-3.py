class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        maps = {}
        for w in words:
            for c in w:
                maps[c] = set()
        
        indegree = {c: 0 for c in maps.keys()}

        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]

            min_word = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:min_word] == word2[:min_word]:
                return ""

            for j in range(min_word):
                if word1[j] != word2[j]:
                    if word2[j] not in maps[word1[j]]:
                        maps[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break

        level = []

        for key in indegree.keys():
            if indegree[key] == 0:
                level.append(key)

        output = []

        while level:
            next_level = []

            for key in level:
                output.append(key)

                for c in maps[key]:
                    indegree[c] -= 1
                    if indegree[c] == 0:
                        next_level.append(c)

            level = next_level

        return "".join(output) if len(output) == len(indegree) else ""

        return ""