class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == s[-j - 1]:
                    dp[i][j] = dp[i-1][j-1] +1 if (i and j) else 1
                else:
                    dp[i][j] = max(dp[i-1][j] * (i > 0), dp[i][j-1] * (j > 0))
        return dp[-1][-1]
        