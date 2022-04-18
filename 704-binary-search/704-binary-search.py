#from bisect import bisect_left

def bisect_left(nums : List[int],target : int) -> int:
    l,r = 0,len(nums)

    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] <= target:
            l = mid
        else: 
            r = mid
            
    return l
    

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        idx = bisect_left(nums,target)
        return idx if idx < len(nums) and nums[idx] == target else -1