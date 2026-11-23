class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        count_s = defaultdict(int)
        count_t = {}

        for i in range(len(t)):
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        best_i = None
        best = float('inf')

        have = 0

        l = 0

        for r in range(len(s)):
            count_s[s[r]] += 1

            if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
                have += 1

            while have == len(count_t):
                if r - l + 1 < best:
                    best = r - l + 1
                    best_i = l

                count_s[s[l]] -= 1

                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1

                l += 1

        return s[best_i:best_i+best] if best_i != None else ""