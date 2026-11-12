class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        window = defaultdict(int)

        left = 0
        best = 0
        count_max = 0

        for right in range(len(s)):
            c = s[right]
            window[c] += 1
            count_max = max(count_max, window[c])

            while right - left + 1 - count_max > k:
                window[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        
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