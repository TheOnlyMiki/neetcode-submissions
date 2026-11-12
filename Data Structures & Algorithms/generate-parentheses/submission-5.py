class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        题目：给定 n 对括号，生成所有合法（有效匹配）的括号组合。
        思路：回溯，每一步决定放 '(' 还是 ')'，只走"可能合法"的分支：
        - 放 '('：只要左括号还没用完（open_count < n）就可以放
        - 放 ')'：必须已放的右括号少于左括号（close_count < open_count），
                  否则会出现没有左括号可以匹配的右括号，如 "())"
        满足这两条规则走到底，得到的字符串一定合法，不需要最后再检查。
        例：n = 2
                         ""
                         |
                        "("
                      /     \
                   "(("     "()"
                    |         |
                  "(()"     "()("
                    |         |
                 "(())"    "()()"
            结果：["(())", "()()"]
        时间复杂度 O(4^n / √n)：合法组合个数是卡特兰数 C(n) ≈ 4^n / (n^1.5 √π)，
                               每个结果拼接字符串需要 O(n)
        空间复杂度 O(n)：递归深度和 path 长度都是 2n（不算输出）

        小提示：
        - 两个判断是 if + if 而不是 if + elif：两个分支可能同时成立，都要尝试。
        - 用列表 path 存字符、最后 "".join，比每次用字符串 path + '(' 拼接更省：
          字符串不可变，每次拼接都会复制一份。
          不过也有人直接传字符串参数 backtrack(path + '(', ...)，
          这样不需要 pop（每层拿到的是新字符串），写起来更短，n 较小时差别不大。
        - 终止条件也可以写成 len(path) == 2 * n：
          因为 close_count <= open_count <= n，长度达到 2n 时两者必然都等于 n。
        - 剪枝的本质：任何前缀中右括号数都不能超过左括号数，
          这也是判断括号字符串是否合法的通用方法（LeetCode 20 用栈，本题只需计数）。
        - 卡特兰数还出现在：不同的二叉搜索树（LeetCode 96）、出栈序列个数等问题中。
        """

        output = []   # 所有合法括号组合

        def backtrack(path, open_count, close_count):
            """
            path       ：当前已生成的括号字符列表
            open_count ：已放入的左括号个数
            close_count：已放入的右括号个数
            """
            # 左右括号都用完了：得到一个完整的合法组合
            if open_count == close_count == n:
                output.append("".join(path))
                return

            # ---------- 分支 1：放左括号 ----------
            # 条件：左括号还没用完
            if open_count < n:
                path.append('(')
                backtrack(path, open_count+1, close_count)
                path.pop()

            # ---------- 分支 2：放右括号 ----------
            # 条件：当前有未匹配的左括号，放入右括号后仍然合法
            if close_count < open_count:
                path.append(')')
                backtrack(path, open_count, close_count+1)
                path.pop()

        backtrack([], 0, 0)

        return output