class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        题目：柱状图中每根柱子宽为 1，高为 heights[i]，求能勾勒出的最大矩形面积。
        核心观察：最大矩形的高度一定等于某一根柱子的高度。
                 对每根柱子 i，以它的高度 heights[i] 为矩形高，尽量往左右延伸：
                 - 往左延伸到"左边第一根比它矮的柱子"之后
                 - 往右延伸到"右边第一根比它矮的柱子"之前
                 宽度 = 右边界 - 左边界 - 1，面积 = heights[i] × 宽度
        问题转化为：对每根柱子，找左右两边第一个比它矮的位置 → 单调栈的经典用途
        例：heights = [2, 1, 5, 6, 2, 3]
            柱子 5（下标 2）：左边第一个更矮的是下标 1，右边第一个更矮的是下标 4
            宽度 = 4 - 1 - 1 = 2，面积 = 5 × 2 = 10（即答案）

        小提示：
        - 三种方法本质相同，都是单调递增栈，时间 O(n)、空间 O(n)。
          每个下标最多入栈、出栈各一次，所以虽然有嵌套 while，总操作数仍是 O(n)。
        - Method 3 最好理解，适合面试时先讲思路；Method 1 / 2 一次遍历，代码更紧凑。
        - 哨兵技巧：在 heights 末尾补一个 0（heights + [0]），
          遍历到最后时这个 0 会把栈里剩下的柱子全部弹出结算，
          就不用再写 Method 1 / 2 结尾那段"处理栈中剩余元素"的代码了。
          同理在栈底预先放一个 -1 作为左哨兵，可以省掉 "if stack else" 的判断。
        - 同类单调栈题：LeetCode 739（每日温度）、42（接雨水）、85（最大矩形，
          把每一行当作柱状图底部，逐行调用本题）。
        """

        # ==================== Method 3 - 两次单调栈分别求左右边界 ====================
        # 时间复杂度 O(n)，空间复杂度 O(n)
        # 思路：从左到右扫一遍求每根柱子"左边第一个更矮的下标"，
        #      从右到左扫一遍求"右边第一个更矮的下标"，最后逐个计算面积

        n = len(heights)

        # ---------- 第 1 步：从左到右，求左边界 ----------
        # 栈中存 (下标, 高度)，从栈底到栈顶高度严格递增
        stack = []
        left_record = [-1] * n   # left_record[i]：左边第一个比 heights[i] 矮的下标，没有则为 -1

        for i in range(n):
            # 栈顶不比当前柱子矮 → 它不可能是 i 的左边界，弹出
            # 而且以后也不会是任何柱子的左边界（i 比它更靠右且不更高，会把它挡住）
            while stack and stack[-1][1] >= heights[i]:
                stack.pop()

            # 弹完后栈顶就是左边第一个比当前矮的柱子；栈空说明左边没有更矮的
            left_record[i] = stack[-1][0] if stack else -1

            stack.append((i, heights[i]))

        # ---------- 第 2 步：从右到左，求右边界 ----------
        # 逻辑与第 1 步完全对称
        stack = []
        right_record = [n] * n   # right_record[i]：右边第一个比 heights[i] 矮的下标，没有则为 n

        for i in range(n-1, -1, -1):
            while stack and stack[-1][1] >= heights[i]:
                stack.pop()

            right_record[i] = stack[-1][0] if stack else n

            stack.append((i, heights[i]))

        # ---------- 第 3 步：以每根柱子为高，计算最大面积 ----------
        output = 0

        for i, h in enumerate(heights):
            # 矩形覆盖 (left_record[i], right_record[i]) 开区间内的所有柱子
            w = right_record[i] - left_record[i] - 1
            output = max(output, h * w)

        return output

        # ==================== Method 2 - 单调栈，栈中记录"可向左延伸的起点" ====================
        # 注意：上面已经 return，以下代码不会执行，仅作对照保留
        # 时间复杂度 O(n)，空间复杂度 O(n)
        # 思路：栈中存 [起点下标, 高度]，表示"高度为 h 的矩形最左可以从起点开始"
        #      遇到更矮的柱子时，栈顶更高的柱子无法再向右延伸，立刻结算它的面积

        stack = []   # 从栈底到栈顶高度非递减
        best = 0

        for i, h in enumerate(heights):
            # 当前柱子默认只能从自己的位置开始
            start_i = i

            # 栈顶比当前柱子高 → 它的矩形在 i 处被截断，右边界确定为 i - 1
            while stack and stack[-1][1] > h:
                pre_i, pre_h = stack.pop()

                # 结算：从 pre_i 延伸到 i - 1，宽度 i - pre_i
                best = max(best, (i - pre_i) * pre_h)

                # 被弹出的柱子都比 h 高，所以当前柱子可以向左延伸到它们的起点
                start_i = pre_i

            # 当前柱子入栈，记录它能向左延伸到的最远起点
            stack.append([start_i, h])

        # 遍历结束后栈中剩余的柱子都能一直延伸到数组末尾
        for i, h in stack:
            best = max(best, (len(heights) - i) * h)

        return best

        # ==================== Method 1 - 单调栈，弹出时结算（经典写法） ====================
        # 时间复杂度 O(n)，空间复杂度 O(n)
        # 思路：栈中只存下标，从栈底到栈顶高度严格递增
        #      某根柱子被弹出时，它的左右边界同时确定：
        #      - 右边界：让它被弹出的当前柱子 i
        #      - 左边界：弹出后新的栈顶（栈是递增的，新栈顶就是左边第一个更矮的柱子）

        stack = []
        best = 0

        for i in range(len(heights)):
            # 栈顶柱子不比当前矮 → 它向右延伸被 i 挡住，弹出并结算
            while stack and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]

                # 宽度 = 右边界 i 与左边界（新栈顶）之间的柱子数
                if stack:
                    w = i - stack[-1] - 1
                else:
                    # 栈空说明左边没有更矮的，可以一直延伸到下标 0
                    w = i

                best = max(best, h * w)

                # 注意：用 >= 弹出时，遇到等高柱子，前一根的面积会被低估（右边界提前了），
                # 但最后一根等高柱子弹出时会算出完整宽度，所以最终答案仍然正确

            stack.append(i)

        # ---------- 处理栈中剩余柱子：它们右边没有更矮的，可以延伸到数组末尾 ----------
        while stack:
            h = heights[stack.pop()]

            if stack:
                w = len(heights) - stack[-1] - 1
            else:
                w = len(heights)

            best = max(best, h * w)

        return best