class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        tree_head = {}
        
        def prefixTreeInsert(node, word):
            for c in word:
                if c not in node:
                    node[c] = {}
                
                node = node[c]

            node['#'] = word

        for word in words:
            prefixTreeInsert(tree_head, word)

        m, n = len(board), len(board[0])

        def dfs(i, j, node):
            if 0 <= i < m and 0 <= j < n and board[i][j] in node:
                c = board[i][j]
                board[i][j] = '.'

                if '#' in node[c]:
                    output.append(node[c].pop('#'))

                for a, b in [(1,0), (0, 1), (-1, 0), (0, -1)]:
                    dfs(i+a, j+b, node[c])

                board[i][j] = c

                if not node[c]:
                    del node[c]

        output = []

        for i in range(m):
            for j in range(n):
                dfs(i, j, tree_head)

        return output

        tree_head = {}
        
        def prefixTreeInsert(node, word):
            for c in word:
                if c not in node:
                    node[c] = {}
                
                node = node[c]

            node['#'] = word

        for word in words:
            prefixTreeInsert(tree_head, word)

        m, n = len(board), len(board[0])

        def dfs(i, j, node):
            if board[i][j] not in node:
                return

            c = board[i][j]

            isWord = node[c].pop('#', False)

            if isWord:
                output.append(isWord)

            board[i][j] = '.'

            for a, b in [(1,0), (0, 1), (-1, 0), (0, -1)]:
                next_i, next_j = i+a, j+b
                if 0 <= next_i < m and 0 <= next_j < n and board[next_i][next_j] != '.':
                    dfs(next_i, next_j, node[c])

            board[i][j] = c

            if not node[c]:
                del node[c]

            return

        output = []

        for i in range(m):
            for j in range(n):
                dfs(i, j, tree_head)

        return output
            