from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 边界条件：如果 s 的长度比 t 还要短，绝对不可能包含 t 的所有字符
        if len(s) < len(t):
            return ""

        # 统计字符串 t 中每个字符出现的频次
        count_t = defaultdict(int)
        for c in t:
            count_t[c] += 1
        
        # 记录当前滑动窗口中各个字符的频次
        window = defaultdict(int)

        # have: 当前窗口中已经满足 count_t 频次要求的**唯一字符数量**
        # need: 字符串 t 中一共包含多少种**不同的字符**
        have, need = 0, len(count_t)
        
        left = 0                               # 滑动窗口的左指针
        min_window = float("infinity")         # 记录最小窗口的长度，初始化为无穷大
        start = -1                             # 记录最小窗口的起始索引位置

        '''while right < len(s):
            c = s[right]
            if c in count_t:
                window[c] += 1
                if window[c] == count_t[c]:
                    have += 1

            while have == need:
                if right - left + 1 < min_window:
                    start = left
                    min_window = right - left + 1

                c_left = s[left]
                window[c_left] -= 1
                if c_left in count_t and window[c_left] < count_t[c_left]:
                    have -= 1

                left += 1

            right += 1'''

        # 遍历右指针，不断扩张窗口
        for right in range(len(s)):
            c = s[right]                       # 当前新滑入窗口右侧的字符
            
            # 如果这个字符是 t 里面的关键字符，才进行处理
            if c in count_t:
                window[c] += 1                 # 将其计入当前窗口的频次中
                # 当窗口内该字符的数量刚好达到 t 所要求的数量时，满足条件的字符种类数 +1
                if window[c] == count_t[c]:
                    have += 1

            # 核心收缩逻辑：只要当前窗口已经包含了 t 中的所有字符（have == need）
            # 就尝试移动左指针来缩小窗口，寻找可能更短的合法子串
            while have == need:
                # 更新全局最小窗口的长度和起始位置
                if right - left + 1 < min_window:
                    start = left
                    min_window = right - left + 1

                c_left = s[left]               # 准备从窗口左侧滑出的字符
                window[c_left] -= 1            # 在窗口记录中减去它的频次
                
                # 如果滑出的字符是 t 里面的关键字符，并且减 1 后导致它的数量不足 t 的要求
                # 那么满足条件的字符种类数 have 就要减 1（从而打破 while 循环，重新去扩张右指针）
                if c_left in count_t and window[c_left] < count_t[c_left]:
                    have -= 1

                left += 1                      # 左指针右移，收缩窗口

        # 如果 start 依然是 -1，说明 s 中没有任何一个子串能覆盖 t
        if start == -1:
            return ""

        # 根据记录的起始位置和最小长度，切片并返回最终的最小子串
        return s[start:start + min_window]
        
        # 时间复杂度 O(n + m): n 和 m 分别是 s 和 t 的长度。右指针遍历一遍 s，左指针最多也遍历一遍 s。
        # 空间复杂度 O(k): k 是字符集的大小（这里最多是 s 和 t 中不同字符的数量），利用了哈希表。

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count_t = defaultdict(int)
        for c in t:
            count_t[c] += 1
        
        window = defaultdict(int)

        have, need = 0, len(count_t)
        left, right = 0, 0
        min_window = float("infinity")
        start = -1

        for right in range(len(s)):
            c = s[right]
            if c in count_t:
                window[c] += 1
                if window[c] == count_t[c]:
                    have += 1

            while have == need:
                if right - left + 1 < min_window:
                    start = left
                    min_window = right - left + 1

                c_left = s[left]
                window[c_left] -= 1
                if c_left in count_t and window[c_left] < count_t[c_left]:
                    have -= 1

                left += 1

        if start == -1:
            return ""

        return s[start:start + min_window]
        # time complexity O(n+m), space complexity O(n)
