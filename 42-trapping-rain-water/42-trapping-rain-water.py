class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)
        
        
        for i in range(len(height)):
            left[i] = max(0 if i == 0 else left[i-1], height[i])
            right[-i - 1] = max(0 if i == 0 else right[-i], height[-i - 1])
        
        #print(left,right)
        return sum(max(0, min(left[i], right[i]) - height[i]) for i in range(len(height)))