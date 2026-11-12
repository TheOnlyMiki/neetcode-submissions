class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        record = defaultdict(int)

        left = 0
        best = 1
        max_count = 0

        for right, c in enumerate(s):
            record[c] += 1
            max_count = max(max_count, record[c])

            while (right - left + 1) - max_count > k:
                record[s[left]] -= 1
                left += 1

            best = max(right - left + 1, best)
            
        return best