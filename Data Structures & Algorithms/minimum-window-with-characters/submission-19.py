class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        
        count_t = {}

        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        left = 0
        start_i = -1
        min_window = float("inf")

        have = 0
        valid = len(count_t)
        window = defaultdict(int)

        for right in range(len(s)):
            c_right = s[right]
            window[c_right] += 1
            if c_right in count_t and window[c_right] == count_t[c_right]:
                have += 1

            while have == valid:
                if right - left + 1 < min_window:
                    min_window = right - left + 1
                    start_i = left

                c_left = s[left]
                window[c_left] -= 1
                if c_left in count_t and window[c_left] < count_t[c_left]:
                    have -= 1

                left += 1

            right += 1
        
        if start_i < 0:
            return  ""

        return s[start_i : start_i + min_window]