class Solution:
    def trap(self, height: List[int]) -> int:
        rr = [[0,0] for _ in range(len(height))] 
        
        
        
        for i in range(len(height)):
            rr[i][0] = max(0 if i == 0 else rr[i-1][0], height[i])
            rr[-i-1][1] = max(0 if i == 0 else rr[-i][1], height[-i - 1])
            
        return sum(max(0,min(rr[i]) - height[i]) for i in range(len(height)))