class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = [0] + list(accumulate(list(map(int,s))))
        end = dp[-1]
        return min(len(s) - i - end + 2 * dp[i] for i in range(len(s) + 1))
            

            