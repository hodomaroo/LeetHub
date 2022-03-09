class Solution(object):
    def maxProduct(self, nums):
        curMax,curMin = 1,1
        res = -float("inf")
        
        for v in nums:
            tmp = curMax * v
            
            curMax = max(curMax * v, curMin * v, v)
            curMin = min(tmp, curMin * v, v)
            res = max(curMax,res)
            
        return res
        
    