class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        _sum = sum(nums)
        
        for i in range(len(nums) - 1, 0, -1):
            _avg = (_sum - 1) // (i + 1)  + 1#평균
            print(_avg)
            diff = nums[i] - _avg
            if diff > 0:
                nums[i - 1] += diff
                nums[i] -= diff
            
            _sum -= nums[i]
        
        print(nums)
        return max(nums)