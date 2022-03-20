class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        ans = []

        for i in range(len(s)):
            dp[i][i] = True
            if not ans: ans = (i, i)

            if i != len(s) - 1 and s[i] == s[i + 1]:
                if ans[1] - ans[0] < 1: ans = (i, i + 1)
                dp[i][i + 1] = True

        for diff in range(2,len(s)):
            for i in range(len(s) - diff):
                if s[i] == s[i + diff] and dp[i + 1][i + diff - 1]:
                    dp[i][i + diff] = True
                    if ans[1] - ans[0] < diff + 1: ans = (i, i + diff)

        return s[ans[0] : ans[1] + 1]
