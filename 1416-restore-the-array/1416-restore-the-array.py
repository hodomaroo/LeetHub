class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (len(s) + 1)
        dp[-2] = 1
        
        
        for i in range(len(s) - 1, -1, -1):
            value = 0
            
            for j in range(i, -1, -1):
                value += pow(10, (i - j)) * int(s[j])
                

                if value > k or (i - j) >= 11: break
                if s[j] == "0" or value == 0: continue
                

                dp[j - 1] = (dp[j - 1] + dp[i]) % MOD
        #print(dp[:-1])
        return dp[-1]
                    
                
                
                
                
                
                
                
                                
  