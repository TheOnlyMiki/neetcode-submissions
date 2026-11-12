class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

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