class TrieNode:
    """
    前缀树节点
    - children：字符 → 子节点
    - isWord  ：从根走到当前节点的路径是否恰好构成一个完整添加过的单词
    """
    def __init__(self):
        self.children = {}
        self.isWord = False


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
                return '#' in node

            if word[i] == '.':
                count += 1

                if count > max_count:
                    return False

                for key in node.keys():
                    if dfs(node[key], i+1, count):
                        return True

            if word[i] not in node:
                return False

            return dfs(node[word[i]], i+1, count)

        return dfs(self.tree_head, 0, 0)

