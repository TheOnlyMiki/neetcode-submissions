
class WordDictionary:
    def __init__(self):
        self.tree_head = {}

    def addWord(self, word: str) -> None:

        if not word:
            return

        node = self.tree_head

        for c in word:
            if c not in node:
                node[c] = {}

            node = node[c]

        node['#'] = word

    def search(self, word: str) -> bool:

        if not word:
            return False

        max_count = 2

        def dfs(node, i, count):
            if i == len(word):
                if '#' in node:
                    return True
                else:
                    return False

            if word[i] == '.':
                if count >= max_count:
                    return False

                for c in node:
                    if dfs(node[c], i+1, count+1):
                        return True

            elif word[i] in node:
                if dfs(node[word[i]], i+1, count):
                    return True

            return False

        return dfs(self.tree_head, 0, 0)

