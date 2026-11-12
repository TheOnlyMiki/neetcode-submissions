class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)

        left = 0
        right = 0

        max_count = 0
        best = 0

        while right < len(s):
            c = s[right]
            window[c] += 1

            max_count = max(max_count, window[c])

            while right - left + 1 - max_count > k:
                window[s[left]] -= 1
                left += 1

            best = max(right - left + 1, best)
            right += 1

        return best