class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        n = len(s1)
        count_s1 = [0] * 26
        window = [0] * 26

        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        match = 0
        for i in range(26):
            if count_s1[i] == window[i]:
                match += 1

        if match == 26:
            return True

        for i in range(len(s1), len(s2)):
            # --- 处理新滑入右侧的字符 ---
            r_idx = ord(s2[i]) - ord('a')
            window[r_idx] += 1
            if window[r_idx] == count_s1[r_idx]:
                match += 1
            elif window[r_idx] == count_s1[r_idx] + 1:
                # 原本是相等的，加了 1 之后导致不相等了，匹配数减 1
                match -= 1

            # --- 处理从左侧滑出的字符 ---
            l_idx = ord(s2[i - len(s1)]) - ord('a')
            window[l_idx] -= 1
            if window[l_idx] == count_s1[l_idx]:
                match += 1
            elif window[l_idx] == count_s1[l_idx] - 1:
                # 原本是相等的，减了 1 之后导致不相等了，匹配数减 1
                match -= 1

            # 检查当前窗口是否完美匹配
            if match == 26:
                return True

        return False
        