class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [[False] * 3 for _ in range(len(nums))] + [[True, True, True]] #[1, 2, 3]
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                dp[i][0] = max(dp[i-2])
            
            if i > 1 and nums[i] == nums[i-1] and nums[i-1] == nums[i-2]:
                dp[i][1] = max(dp[i-3])
            
            if i > 1 and nums[i] == nums[i-1] + 1 and nums[i - 2] + 1 == nums[i - 1]:
                dp[i][2] = max(dp[i-3])
        
        return max(dp[-2])
                
                
            