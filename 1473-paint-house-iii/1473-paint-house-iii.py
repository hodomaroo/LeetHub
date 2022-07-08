from typing import List

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:        
        dp = [[[float("inf") for _ in range(n)] for _ in range(target + 1)] for _ in range(2)]
        for i in range(m):
            if houses[i]:
                cost[i][houses[i] - 1] = 0
        #m : house n : color target : limit neighbor
        #dp[house][neighborhood][color]
        
        
        
        dp[1][0] = [0] * n

        for house in range(m):
            dp[house%2][0] = [float("inf")] * n
            
            for neighbor in range(1, target + 1):    
                dp[house%2][neighbor] = [float("inf")] * n
            
                for color in (range(n) if not houses[house] else [houses[house] - 1]):
                    dp[house%2][neighbor][color] = min(dp[house%2][neighbor][color], dp[1 - house%2][neighbor][color] + cost[house][color],
                                                     min(dp[1 - house%2][neighbor - 1][i] for i in range(n) if i != color) + cost[house][color])  
        ans = min(dp[(m-1)%2][target]) 
        return ans if ans != float("inf") else -1
                    
                    



