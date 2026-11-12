class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.tree_head = TrieNode()

    def addWord(self, word: str) -> None:
        
        if not word:
            return

        current = self.tree_head

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.isWord = True


    def search(self, word: str) -> bool:
        
        if not word:
            return False

        current = self.tree_head

        def dfs(node, i, count):
            if i == len(word):
                return node.isWord

            if word[i] == '.':
                count += 1

                if count > 2:
                    return False
                
                for c in node.children:
                    if dfs(node.children[c], i+1, count):
                        return True

            else:
                if word[i] not in node.children:
                    return False
                
                if dfs(node.children[word[i]], i+1, count):
                    return True

            return False

        return dfs(self.tree_head, 0, 0)
