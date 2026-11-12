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
            