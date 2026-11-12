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
