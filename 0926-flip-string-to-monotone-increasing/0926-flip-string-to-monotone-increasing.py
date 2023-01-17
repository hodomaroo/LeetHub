class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = [0] + list(accumulate(list(map(int,s))))
        
        #i부터 1로 만든다
        
#         print(dp)
        
#         for i in range(len(s) + 1):
#             #i번째까지 1로 채운다면, 아래 개수만큼 필요
#             print(len(s) - i - (dp[-1] - dp[i]),dp[i])
            
        return min(len(s) - i - (dp[-1] - dp[i]) + dp[i] for i in range(len(s) + 1))
            

            