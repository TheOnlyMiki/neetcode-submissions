class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        题目：给定仅包含数字 2-9 的字符串，按电话按键映射，返回所有可能的字母组合（顺序任意）。
        思路：每一位数字对应 3~4 个字母，从每一位里各选一个字母拼起来 → 笛卡尔积
        - Method 2 迭代：逐位扩展，每多一位数字，就把已有的每个组合分别接上该数字的每个字母
        - Method 1 回溯：第 i 层决定第 i 位数字选哪个字母，走到底就是一个完整组合
        例：digits = "23"
            "2" → ["a", "b", "c"]
            "3" → ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        时间复杂度 O(4^n · n)：n 为 digits 长度，最多 4^n 个组合，每个拼接 O(n)
        空间复杂度：Method 2 中间结果 O(4^n · n)；Method 1 递归深度 O(n)（不算输出）

        小提示：
        - 原迭代写法的映射里 "7" 写成了 "qprs"，已改为 "pqrs"。
          因为题目允许任意顺序输出，写错顺序也能通过，但映射本身应保持正确。
        - digits 为空时必须返回 []，而不是 [""]：
          迭代写法 res 初始是 [""]，回溯写法第一层就满足长度条件会加入 ""，都需要提前特判。
        - 回溯的终止条件也可以写成 i == len(digits)，和 len(path) == len(digits) 等价。
        - 这题每一层的选择互不影响，不需要剪枝，也不需要去重，是回溯最基础的形式。
        - 标准库写法：itertools.product 直接求笛卡尔积
              return ["".join(p) for p in itertools.product(*(maps[d] for d in digits))]
        """

        # ==================== Method 2 - 迭代（逐位扩展） ====================

        if not digits:
            return []

        # 初始只有一个空组合，作为第一位扩展的基础
        res = [""]

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        for digit in digits:
            tmp = []   # 加入当前数字后的新组合
            # 已有的每个组合，分别接上当前数字对应的每个字母
            for curStr in res:
                for c in digitToChar[digit]:
                    tmp.append(curStr + c)
            res = tmp

        return res

        # ==================== Method 1 - 回溯 ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留

        if not digits:
            return []

        output = []   # 所有字母组合

        maps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(i, path):
            """
            i   ：当前要处理第 i 位数字
            path：已选的字母（长度为 i）
            """
            # 每一位数字都选好了字母：得到一个完整组合
            if len(path) == len(digits):
                output.append("".join(path))
                return

            # 枚举第 i 位数字对应的每个字母
            for c in maps[digits[i]]:
                path.append(c)          # 做选择

                backtrack(i+1, path)    # 递归：处理下一位数字

                path.pop()              # 撤销选择，尝试下一个字母

        backtrack(0, [])

        return output