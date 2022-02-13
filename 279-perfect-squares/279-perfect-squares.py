from math import sqrt

class Solution(object):
    def numSquares(self, n):
        dp = [0 for _ in range(n+1)]
        for i in range(1,n+1):
            if sqrt(i) == int(sqrt(i)): dp[i] = 1
            else:
                dp[i] = min(dp[i-(root**2)] for root in range(1,int(sqrt(i)) + 1)) +1
        return dp[n]


