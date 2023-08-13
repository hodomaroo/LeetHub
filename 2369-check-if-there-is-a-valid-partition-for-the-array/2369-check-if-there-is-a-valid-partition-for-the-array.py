class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))] + [True] #[1, 2, 3]
        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i-2] if nums[i] == nums[i-1] else False,  dp[i-3] if i > 1 and ((nums[i] == nums[i-1] and nums[i-1] == nums[i-2]) or (nums[i-1] + 1 == nums[i] and nums[i-2] + 1 == nums[i-1])) else False)
        
        return dp[-2]
                
                
            