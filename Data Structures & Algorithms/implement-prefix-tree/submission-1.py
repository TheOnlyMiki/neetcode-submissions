class TrieNode:
    """
    前缀树节点
    - children：字符 → 子节点，表示从当前节点沿这个字符往下走
    - isWord  ：从根走到当前节点的路径，是否恰好构成一个"完整插入过的单词"
    注意：节点本身不存字符，字符存在"边"上（即 children 的 key）
    """
    def __init__(self):
        self.children = {}
        self.isWord = False


class PrefixTree:
    """
    题目：实现前缀树（Trie，LeetCode 208），支持：
         - insert(word)：插入单词
         - search(word)：判断单词是否被完整插入过
         - startsWith(prefix)：判断是否有已插入的单词以 prefix 开头
    思路：每个单词是从根出发的一条路径，共享相同前缀的单词共享同一段路径。
    例：插入 "app"、"apple"、"bat"
                root
               /    \
              a      b
              |      |
              p      a
              |      |
              p*     t*
              |
              l
              |
              e*
        （* 表示 isWord = True）
        search("app") → True；search("ap") → False（路径存在但不是完整单词）
        startsWith("ap") → True（路径存在即可）
    复杂度（L 为单词 / 前缀长度）：
    - insert / search / startsWith：时间 O(L)，与已存单词数量无关
    - 空间：最坏 O(所有单词总长度)，共享前缀越多越省

    小提示：
    - search 和 startsWith 唯一的区别在最后一行：
      search 要求走到的节点 isWord 为 True，startsWith 只要求路径存在。
      两者前半段完全相同，可以抽成一个辅助方法复用：
          def _find(self, s):
              current = self.tree_head
              for c in s:
                  if c not in current.children:
                      return None
                  current = current.children[c]
              return current
          search     → node = self._find(word);   return node is not None and node.isWord
          startsWith → return self._find(prefix) is not None
    - 空字符串的处理：题目保证长度 >= 1，所以特判不影响结果。
      但从定义上说，任何单词都以空前缀开头，startsWith("") 更合理的返回值是 True
      （只要插入过单词）；去掉特判后代码会自然返回 True。
    - children 也可以用长度 26 的数组（下标 ord(c) - ord('a')），
      访问更快但每个节点固定占 26 个位置；用字典则只存实际出现的字符，更省空间也更通用。
    - Trie 相关题：
      · LeetCode 211（添加与搜索单词）：search 支持通配符 '.'，遇到 '.' 时 DFS 所有子节点
      · LeetCode 212（单词搜索 II）：把所有单词建成 Trie，在网格上 DFS 时同步在 Trie 上往下走
    """

    def __init__(self):
        # 根节点：不代表任何字符，是所有单词路径的起点
        self.tree_head = TrieNode()

    def insert(self, word: str) -> None:

        # 空单词不插入
        if not word:
            return

        current = self.tree_head

        # 沿着单词的字符一路往下走，没有的边就新建节点
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        # 走到单词最后一个字符对应的节点，标记这里是一个完整单词的结尾
        current.isWord = True

    def search(self, word: str) -> bool:

        if not word:
            return False

        current = self.tree_head

        # 沿着单词的字符往下走，中途断了说明这个单词（及其前缀）从未插入过
        for c in word:
            if c not in current.children:
                return False

            current = current.children[c]

        # 路径存在还不够，必须是某个插入单词的结尾
        # 例：只插入了 "apple"，search("app") 路径存在但 isWord 为 False
        return current.isWord

    def startsWith(self, prefix: str) -> bool:

        if not prefix:
            return False

        current = self.tree_head

        # 和 search 一样沿路径往下走
        for c in prefix:
            if c not in current.children:
                return False

            current = current.children[c]

        # 路径能走完，就说明至少有一个插入的单词以 prefix 开头
        return True