class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        #baseCase -> 다 선택한경우 
        dp = [[float("-inf")] * (len(multipliers) + 1) for _ in range(len(multipliers) + 1)]
        
        for i in range(len(multipliers) + 1):
            dp[i][len(multipliers) - i] = 0
            
        for i in range(len(multipliers) - 1, -1, -1):
            for left in range(i + 1):
                right = i - left                
                dp[left][right] = max(dp[left + 1][right] + nums[left] * multipliers[left + right],dp[left][right + 1] + nums[-right - 1] * multipliers[left + right])
                    
        return dp[0][0]
        
            
            
            