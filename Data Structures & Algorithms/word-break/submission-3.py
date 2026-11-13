class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)

        dp = [False] * (n+1)
        dp[0] = True

        wordDict = set(wordDict)

        max_length, min_length = 0, float('inf')

        for word in wordDict:
            max_length = max(max_length, len(word))
            min_length = min(min_length, len(word))

        for i in range(1, n+1):
            start = max(0, i - max_length)
            end = i - min_length + 1

            for j in range(start, end):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]