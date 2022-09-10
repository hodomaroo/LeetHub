from time import monotonic


class Solution:
    def maxProfit(self, k: int, prices : list[int]) -> int:
        
        monotonic = []
        
        points = []
        
        for v in prices + [-1001]:
            if not monotonic or monotonic[-1] > v:
                if len(monotonic) > 1:
                    points.extend([monotonic[0],monotonic[-1]])
                monotonic = [v]
                
            if monotonic[-1] < v:
                monotonic.append(v)
        #k번의 트랜잭션으로 얻을 수 있는 최대 이득
        #근데 그냥
        
        dp = [[0] * (k + 1) for _ in range(len(points))] #포인트별로 k번의 트랜잭션
        if not k or len(points) < 1:
            return 0
        
        maxi = 0
        MAX = 0
        #points[j] - points[i] + dp[i][k] # --> points[i] + dp[i][k-1]
        for i in range(1, k + 1):
            MAX = - points[0]
            for j in range(1,len(points)):
                dp[j][i] = max(dp[j-1][i], points[j] + MAX)
                MAX = max(-points[j] +  dp[j][i - 1],MAX)
                maxi = max(maxi, dp[j][i])
        
        return maxi
                    
            
                
                
            
            
            
    
        
        
        
        
        
        