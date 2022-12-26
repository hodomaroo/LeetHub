class Solution:
    def canJump(self, nums: List[int]) -> bool:
        _max = 0
        
        for i in range(len(nums)):
            if _max < i:
                return False
            
            _max = max(i + nums[i] , _max)
            
        return True