class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        题目：外星语言使用英文小写字母，但字母顺序未知。给定一个按外星字典序排好序的单词列表，
             推断出字母顺序并返回（任意一种合法顺序即可）；如果顺序矛盾（无效），返回 ""。
             即 LeetCode 269（火星词典）。
        思路：建图 + 拓扑排序（和 LeetCode 207 / 210 课程表同一个框架）
        - 节点：所有出现过的字母
        - 边：比较相邻两个单词，第一个不同的字母决定先后，word1[j] 排在 word2[j] 前面 → 边 word1[j] → word2[j]
          第一个不同位置之后的字母不提供任何顺序信息（就像 "ab" < "ba" 只说明 a < b，不说明 b 和 a 的第二位关系）
        - 对图做拓扑排序：能排完所有字母就是答案；有环说明顺序矛盾
        例：words = ["wrt", "wrf", "er", "ett", "rftt"]
            "wrt" vs "wrf"：t → f
            "wrf" vs "er" ：w → e
            "er"  vs "ett"：r → t
            "ett" vs "rftt"：e → r
            得到 w → e → r → t → f，答案 "wertf"
        复杂度（C 为所有单词的总字符数，U 为不同字母数，最多 26）：
        - 建图：O(C)，每对相邻单词最多比较到较短单词的长度
        - 拓扑排序：O(U + E)，E 最多 U²
        - 空间：O(U + E)

        小提示：
        - 两种无效情况都要处理：
          · 前缀矛盾：word1 比 word2 长且 word2 是 word1 的前缀（如 ["abc", "ab"]），
            正常字典序中短的前缀一定排在前面，这种输入本身就不合法，直接返回 ""
          · 顺序成环：如 a → b 又 b → a，拓扑排序无法排完所有字母，最后检查 len(output)
        - 只需要比较"相邻"的单词：字典序有传递性，word1 < word2 < word3 时，
          word1 和 word3 的关系已经能从两对相邻比较中推出来，不用两两比较所有单词。
        - 边要去重（if word2[j] not in maps[word1[j]]）：同一条边如果被加两次，
          入度会多加一次，但邻接集合里只有一条边，入度永远减不到 0，会误判成有环。
          用 set 存邻居 + 先判断再加入度，正好避免了这个问题。
        - 所有出现过的字母都要先放进 maps 和 indegree，
          包括没有任何先后信息的字母（入度为 0，它们可以出现在答案的任意位置）。
        - break 很关键：只有第一个不同的字母提供顺序信息，找到后立刻停止比较。
        - DFS 写法：三色标记判环，后序收集字母，最后反转得到拓扑序。
        """

        # ---------- 第 1 步：收集所有出现过的字母，作为图的节点 ----------
        # maps[c]：必须排在 c 后面的字母集合（邻接表，用 set 去重）
        maps = {}
        for w in words:
            for c in w:
                maps[c] = set()

        # 每个字母的入度：有多少个字母必须排在它前面
        indegree = {c: 0 for c in maps.keys()}

        # ---------- 第 2 步：比较相邻单词，建立字母之间的先后关系 ----------
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]

            min_word = min(len(word1), len(word2))

            # 前缀矛盾：较长的 word1 排在它自己的前缀 word2 之前，输入无效
            if len(word1) > len(word2) and word1[:min_word] == word2[:min_word]:
                return ""

            # 找第一个不同的字母
            for j in range(min_word):
                if word1[j] != word2[j]:
                    # word1[j] 排在 word2[j] 前面：加边 word1[j] → word2[j]（去重，避免入度多算）
                    if word2[j] not in maps[word1[j]]:
                        maps[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    # 后面的字母不提供顺序信息
                    break

        # ---------- 第 3 步：拓扑排序（Kahn 算法，按层 BFS） ----------
        # 入度为 0 的字母：没有必须排在它前面的字母，可以先放
        level = []

        for key in indegree.keys():
            if indegree[key] == 0:
                level.append(key)

        output = []   # 字母顺序（拓扑序）

        while level:
            next_level = []

            for key in level:
                output.append(key)

                # key 已放好，排在它后面的字母少了一个前置约束
                for c in maps[key]:
                    indegree[c] -= 1
                    # 前置约束全部满足，下一轮可以放
                    if indegree[c] == 0:
                        next_level.append(c)

            level = next_level

        # 没能排完所有字母：存在环，顺序矛盾
        if len(output) != len(indegree):
            return ""

        return ''.join(output)