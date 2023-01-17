class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp,leng = [0] + list(accumulate(list(map(int,s)))),len(s)
        end = dp[-1]
        return min(leng - i - end + 2 * dp[i] for i in range(len(s) + 1))
            

            