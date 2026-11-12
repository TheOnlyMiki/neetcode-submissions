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
    """
    题目：设计数据结构（LeetCode 211），支持：
         - addWord(word)：添加单词
         - search(word)：判断是否存在匹配的单词，word 中的 '.' 可以匹配任意一个字母
    思路：前缀树（Trie）+ DFS
    - addWord 和 LeetCode 208 的 insert 完全一样
    - search 遇到普通字母：只能沿这个字母的边往下走（和 208 一样）
    - search 遇到 '.'：当前节点的每个子节点都可能匹配，需要逐个尝试 → DFS 回溯
    例：添加 "bad"、"dad"、"mad"
        search("pad") → False
        search(".ad") → True（'.' 尝试 b、d、m，走 b 时 "ad" 能匹配）
        search("b..") → True
    复杂度（L 为单词长度，d 为 '.' 的个数）：
    - addWord：O(L)
    - search：无 '.' 时 O(L)；有 '.' 时最坏 O(26^d · L)，每个 '.' 最多分出 26 个分支

    小提示：
    - count 参数（限制 '.' 最多 2 个）其实没有必要：
      题目约束只是说测试数据里 '.' 最多 2 个，并不是"超过 2 个就不匹配"。
      保留它在题目约束下不影响结果，但如果 '.' 更多，会把本应匹配的单词错误地判为 False。
      去掉 count 后 dfs(node, i) 两个参数就够了。
    - search 里的 current = self.tree_head 没有用到，可以删掉。
    - 普通字母分支可以直接写成 return dfs(node.children[word[i]], i + 1, count)，
      不需要 if ... return True 再在外面 return False。
    - 优化思路：可以按单词长度分组存放，或在节点里记录"子树中单词的长度集合"，
      搜索时提前排除长度不可能匹配的分支；面试一般不要求。
    - 进阶题 LeetCode 212（单词搜索 II）：Trie 的 DFS 从"在 Trie 上分叉"
      变成"在网格上分叉、同步在 Trie 上往下走"。
    """

    def __init__(self):
        # 根节点：不代表任何字符
        self.tree_head = TrieNode()

    def addWord(self, word: str) -> None:

        if not word:
            return

        current = self.tree_head

        # 沿单词字符一路往下走，没有的边就新建节点
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        # 标记单词结尾
        current.isWord = True

    def search(self, word: str) -> bool:

        if not word:
            return False

        current = self.tree_head

        def dfs(node, i, count):
            """
            node ：当前所在的 Trie 节点（已匹配完 word[:i]）
            i    ：下一个要匹配的字符下标
            count：剩余可用的 '.' 个数
            返回从 node 出发能否匹配 word[i:]
            """
            # word 全部匹配完，还要求停在某个完整单词的结尾
            if i == len(word):
                return node.isWord

            # ---------- 情况 1：通配符 '.'，可以匹配任意一个子节点 ----------
            if word[i] == '.':
                count -= 1

                # 超过允许的 '.' 个数（题目约束下不会触发）
                if count < 0:
                    return False

                # 逐个尝试所有子节点，有一个能匹配剩余部分就成功
                for c in node.children:
                    if dfs(node.children[c], i+1, count):
                        return True

            # ---------- 情况 2：普通字母，只能走对应的那条边 ----------
            else:
                # 没有这条边，匹配失败
                if word[i] not in node.children:
                    return False

                if dfs(node.children[word[i]], i+1, count):
                    return True

            # 所有可能的分支都失败
            return False

        # 从根节点、word 第 0 个字符开始匹配，最多允许 2 个 '.'
        return dfs(self.tree_head, 0, 2)