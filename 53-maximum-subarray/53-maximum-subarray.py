class Solution(object):
    def maxSubArray(self, nums):
        maximum = -(int(1e10))
        nowSum = 0
        #print(maximum)

        for v in nums:
            nowSum = v if nowSum < 0 else nowSum + v
            maximum = max(nowSum,maximum)
        return maximum


