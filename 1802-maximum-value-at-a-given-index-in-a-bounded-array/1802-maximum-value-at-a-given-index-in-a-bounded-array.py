class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l,r = 0, maxSum + 1
        
        while l + 1 < r:
            mid = (l + r) // 2
            
            left_sum = (mid) * (mid + 1) // 2
            right_sum = (mid) * (mid + 1) // 2
            
            if index >= mid:
                left_sum += index - mid + 1
            if index + 1 < mid:
                left_sum -= (mid - index - 1) * (mid - index) // 2
            
            if n - index > mid:
                right_sum += n - index - mid
            
            if n - index < mid:
                right_sum -= (mid - (n - index)) * (mid - (n - index) + 1) // 2
            
            #print(left_sum, right_sum, mid)
            if left_sum + right_sum - mid > maxSum:
                r = mid
            else:
                l = mid
                
        return l