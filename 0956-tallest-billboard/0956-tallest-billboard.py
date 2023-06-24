class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 0
        
        
        for v in rods:
            cur = defaultdict(int)
            
            for vv in dp:
                cur[vv + v] = max(cur[vv + v],  dp[vv] + v)
                cur[vv] = max(cur[vv],  dp[vv])
                cur[vv - v] = max(cur[vv - v], dp[vv])
                
            dp = cur
            #print(dp)
        return dp[0]
                        
            
                
        