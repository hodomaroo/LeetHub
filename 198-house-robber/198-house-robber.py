class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0,0] for _ in range(len(nums) + 1)]
        
        #dp[i][0] -> not select
        #dp[i][1] -> select
        for i in range(1, len(nums) + 1):
            dp[i][0] = max(dp[i-1])
            dp[i][1] = dp[i-1][0] + nums[i - 1]
        return max(dp[-1])