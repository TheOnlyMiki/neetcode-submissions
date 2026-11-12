class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1 = [0] * 26
        window = [0] * 26
        # 计数 s1 和 s2 里的 window 的次数
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        # 如果一致就代表开头就找到了
        if count_s1 == window:
            return True

        # 现在移动窗口，[a b c] d -> a [b c d]
        for i in range(len(s1), len(s2)):
            # 新进来的+1
            window[ord(s2[i]) - ord('a')] += 1
            # 挪出去的-1
            window[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if count_s1 == window:
                return True

        return False
        # time complexity O(n+m), space complexity O(1)

        # 能否把每次滑动时 O(26) 的数组比较优化到真正的 O(1)
        if len(s1) > len(s2):
            return False
        
        count_s1 = [0] * 26
        window = [0] * 26
        
        # 1. 统计 s1 和 s2 前 len(s1) 个字符的频次
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        # 2. 初始化 matches 的数量（检查有多少个字母的频次一开始就匹配）
        matches = 0
        for i in range(26):
            if count_s1[i] == window[i]:
                matches += 1

        # 如果 26 个字母的频次全部吻合，说明开头就找到了
        if matches == 26:
            return True

        # 3. 开始滑动窗口
        for i in range(len(s1), len(s2)):
            # --- 处理新滑入右侧的字符 ---
            r_idx = ord(s2[i]) - ord('a')
            window[r_idx] += 1
            if window[r_idx] == count_s1[r_idx]:
                matches += 1
            elif window[r_idx] == count_s1[r_idx] + 1:
                # 原本是相等的，加了 1 之后导致不相等了，匹配数减 1
                matches -= 1

            # --- 处理从左侧滑出的字符 ---
            l_idx = ord(s2[i - len(s1)]) - ord('a')
            window[l_idx] -= 1
            if window[l_idx] == count_s1[l_idx]:
                matches += 1
            elif window[l_idx] == count_s1[l_idx] - 1:
                # 原本是相等的，减了 1 之后导致不相等了，匹配数减 1
                matches -= 1

            # 检查当前窗口是否完美匹配
            if matches == 26:
                return True

        return False

            