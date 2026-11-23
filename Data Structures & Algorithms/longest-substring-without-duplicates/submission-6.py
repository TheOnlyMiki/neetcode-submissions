class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res

        n = len(s)
        
        l, r = 0, 0

        output = 0

        window = set()

        while r < n:

            if s[r] not in window:
                window.add(s[r])
                output = max(output, r-l+1)
                r += 1
            else:
                window.remove(s[l])
                l += 1

        return output

        # Method 1 - two pointer
        output = 0
        record = set()
        left = 0

        for right, c in enumerate(s):
            while c in record:
                record.remove(s[left])
                left += 1
            record.add(c)
            
            length = right - left + 1
            if length > output:
                output = length

        return output
        # time complexity O(n), space complexity O(n)
