class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = [0] + list(accumulate(list(map(int,s))))
        return min(len(s) - i - dp[-1] + 2 * dp[i] for i in range(len(s) + 1))
            

            