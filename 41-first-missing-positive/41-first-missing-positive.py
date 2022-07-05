class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums += [0]
        for v in nums:
            if v <= 0 or v >= len(nums) or nums[v] == v : continue
            
            
            tmp = nums[v]
            
            while tmp < len(nums) and nums[v] != v and nums[v] > 0 and nums[nums[v]] != nums[v]:   
                nums[v] = v
                v = tmp
                tmp = nums[v]
                
            nums[v] = v
    
        print(nums)
        for i in range(1, 500002):
            if i >= len(nums) or nums[i] != i:
                return i
            
