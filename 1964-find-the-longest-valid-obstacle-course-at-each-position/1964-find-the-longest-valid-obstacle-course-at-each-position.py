class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        stk = []
        dp = [1] * len(obstacles)
        
        for i,v in enumerate(obstacles):
            pos = bisect_left(stk, v + 1)
            
            if pos == len(stk): stk.append(v)
            else:   stk[pos] = v
            
            dp[i] = pos + 1
        return dp
            