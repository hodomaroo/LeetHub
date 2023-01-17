class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp,leng = [0] + list(accumulate(list(map(int,s)))),len(s)
        return min(leng - i - dp[-1] + 2 * dp[i] for i in range(len(s) + 1))
            

            