class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 3)

        for i in range(len(cost) + 1):
            dp[i] = min(dp[i - 1], dp[i - 2]) + (cost[i] if i < len(cost) else 0) 
        return dp[-3]


