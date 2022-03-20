class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        ans = ""

        for i in range(len(s)):
            dp[i][i] = True
            if not ans: ans = s[i]

            if i != len(s) - 1 and s[i] == s[i + 1]:
                if len(ans) < 2: ans = s[i: i + 2]
                dp[i][i + 1] = True

        for diff in range(2,len(s)):
            for i in range(len(s) - diff):
                if s[i] == s[i + diff] and dp[i + 1][i + diff - 1]:
                    dp[i][i + diff] = True
                    if len(ans) < diff + 1: ans = s[i: i + diff + 1]
        return ans
