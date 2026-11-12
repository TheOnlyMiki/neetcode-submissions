class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class PrefixTree:

    def __init__(self):
        self.tree_head = TrieNode()

    def insert(self, word: str) -> None:

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

        for c in word:
            if c not in current.children:
                return False

            current = current.children[c]

        return current.isWord

    def startsWith(self, prefix: str) -> bool:
        
        if not prefix:
            return False

        current = self.tree_head

        for c in prefix:
            if c not in current.children:
                return False
            
            current = current.children[c]

        return True

        