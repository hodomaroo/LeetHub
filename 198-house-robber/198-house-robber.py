class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0,0] for _ in range(len(nums) + 2)]
        
        #dp[i][0] -> not select
        #dp[i][1] -> select
        for i in range(2, len(nums) + 2):
            dp[i][0] = max(dp[i-2][0] + nums[i-2], dp[i-1][0])
            
        return dp[-1][0]