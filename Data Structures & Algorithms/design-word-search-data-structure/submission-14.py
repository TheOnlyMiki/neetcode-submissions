

class WordDictionary:
    def __init__(self):
        # 根节点：不代表任何字符
        self.tree_head = {}

    def addWord(self, word: str) -> None:

        if not word:
            return

        current = self.tree_head

        for c in word:
            if c not in current:
                current[c] = {}
            
            current = current[c]

        current['#'] = word

    def search(self, word: str) -> bool:

        if not word:
            return False

        def dfs(node, i, count, count_max):
            if i == len(word):
                return '#' in node

            if word[i] == '.' and count < count_max:
                for c in node.keys():
                    if c == '#':
                        continue

                    if dfs(node[c], i+1, count+1, count_max):
                        return True
            
            if word[i] not in node:
                return False

            if dfs(node[word[i]], i+1, count, count_max):
                return True

            return False

        return dfs(self.tree_head, 0, 0, 2)
