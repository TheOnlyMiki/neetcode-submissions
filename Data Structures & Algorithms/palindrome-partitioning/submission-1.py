class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        题目：把字符串 s 分割成若干子串，使每个子串都是回文串，返回所有可能的分割方案。
        思路：回溯。把"切割"看成"选择每一段的结束位置"：
        - 当前段从 start 开始，枚举结束位置 end（start ~ len(s)-1）
        - s[start..end] 是回文 → 切下这一段，从 end + 1 开始继续切下一段
        - start 走到字符串末尾 → 整个字符串都被切成回文段，记录一种方案
        和组合问题同一个框架：这里的"选数"变成了"选切割点"。
        例：s = "aab"
                              start=0
                     /           |           \
                   "a"          "aa"         "aab"（不是回文，剪掉）
                    |            |
                 start=1      start=2
                 /     \         |
               "a"    "ab"✗     "b"
                |                |
             start=2          结束 → ["aa","b"]
                |
               "b"
                |
             结束 → ["a","a","b"]
        时间复杂度 O(n · 2^n)：n - 1 个间隙每个切或不切，最多 2^n 种方案，
                             每种方案判断回文、复制结果都需要 O(n)
        空间复杂度 O(n)：递归深度和 path 长度（不算输出）

        小提示：
        - 优化：同一个子串 s[i..j] 会在不同分支里被反复判断是否回文，
          可以先用动态规划预处理一个 n × n 的表，之后 O(1) 查询：
              n = len(s)
              dp = [[False] * n for _ in range(n)]
              for i in range(n - 1, -1, -1):          # i 从后往前，保证 dp[i+1][j-1] 已算好
                  for j in range(i, n):
                      dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])
          然后把 isPalindrome(start, end) 换成 dp[start][end]。
          dp 含义：两端字符相同，且去掉两端后剩下的部分也是回文（长度 <= 2 时中间为空或单字符，直接成立）。
          预处理 O(n²)，最坏情况总复杂度不变，但实际运行快很多。
        - 判断回文也可以用切片 sub == sub[::-1]，写法更短，但每次要复制子串。
        - 进阶题 LeetCode 132（分割回文串 II）：求最少切几刀，不需要列出所有方案，
          要用动态规划而不是回溯，否则会超时。
        """

        def isPalindrome(left, right):
            """判断 s[left..right] 是否是回文：双指针从两端向中间比较"""
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        output = []   # 所有分割方案

        def backtrack(start, path):
            """
            start：当前段的起始位置，s[:start] 已经被切成回文段
            path ：已切下的回文段
            """
            # 已经切到字符串末尾：得到一个完整方案（必须复制）
            if start == len(s):
                output.append(path[:])
                return

            # 枚举当前段的结束位置
            for end in range(start, len(s)):
                # 只有当前段是回文才能切（剪枝：不是回文的分支直接放弃）
                if isPalindrome(start, end):
                    path.append(s[start:end+1])   # 做选择：切下 s[start..end]

                    backtrack(end+1, path)        # 递归：从下一个位置开始切下一段

                    path.pop()                    # 撤销选择，尝试更长的一段

        backtrack(0, [])

        return output