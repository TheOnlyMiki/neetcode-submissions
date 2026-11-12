class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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