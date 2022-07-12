class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        dp = [-1] * pow(2, len(matchsticks))

        s = sum(matchsticks)
        mod,rem = s // 4, s % 4
        
        if rem or mod < max(matchsticks): return False
        
        def dfs(stat : int) -> int:
            if dp[stat] != -1: return dp[stat]
            if not stat: return 0
            
                
            
            for i in range(len(matchsticks)):
                if stat >> i & 1: 
                    rem = dfs(stat ^ (1 << i))
                    if rem >= 0 and matchsticks[i] + rem <= mod:
                        #print(stat,(matchsticks[i] + rem) % mod)
                        dp[stat] = (matchsticks[i] + rem) % mod
                        return (matchsticks[i] + rem) % mod
            dp[stat] = -2
            return -1
        #dfs(pow(2,len(matchsticks)) - 1)
        return [True,False][dfs(pow(2,len(matchsticks)) - 1) != 0]
                              
                    
                