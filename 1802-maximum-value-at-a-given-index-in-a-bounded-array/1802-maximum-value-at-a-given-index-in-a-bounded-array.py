class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l,r = 0, maxSum + 1
        
        while l + 1 < r:
            mid = (l + r) // 2
            
            _sum = (mid) * (mid + 1) - mid
            
            if index >= mid:
                _sum += index - mid + 1
            
            if index + 1 < mid:
                _sum -= (mid - index - 1) * (mid - index) // 2
            
            if n - index > mid:
                _sum += n - index - mid
            
            if n - index < mid:
                _sum -= (mid - (n - index)) * (mid - (n - index) + 1) // 2
        
            if _sum > maxSum:
                r = mid
            else:
                l = mid
                
        return l