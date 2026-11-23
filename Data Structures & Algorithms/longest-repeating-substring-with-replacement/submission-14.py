class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        window = defaultdict(int)

        l, r = 0, 0

        max_count = 0

        best = 0

        for r in range(len(s)):

            window[s[r]] += 1

            max_count = max(max_count, window[s[r]])

            while l < r and r-l+1 - max_count > k:
                window[s[l]] -= 1
                l += 1

            best = max(best, r-l+1)

        return best

            










































        # Method 1 - slide window
        record = defaultdict(int)

        left = 0
        best = 1
        max_count = 0

        for right in range(len(s)):
            record[s[right]] += 1
            max_count = max(max_count, record[s[right]])

            # 窗口长度 − 窗口内最多的字符数 = 需要替换的个数。
            while (right - left + 1) - max_count > k:
                record[s[left]] -= 1
                left += 1

            best = max(right - left + 1, best)
            
        return best
        # time complexity O(n), space complexity O(m)