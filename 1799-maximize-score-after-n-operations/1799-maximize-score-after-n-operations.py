class Solution:
    def maxScore(self, nums: List[int]) -> int:
        dp = [-1] * (2 ** len(nums))
        dp[-1] = 0
    
        def top_down(status : int, depth : int) -> int:    
            if dp[status] != -1:  return dp[status]
            
            for i in range(len(nums)):
                if (status >> i) & 1: continue
                
                for j in range(i + 1, len(nums)):
                    if (status >> j) & 1: continue
                
                    dp[status] = max(dp[status], top_down(status | (1 << i) | (1 << j), depth + 1) + gcd(nums[i], nums[j]) * depth)
                    
            return dp[status]
            
        return top_down(0,1)    
            
        
        
        