from typing import List
from itertools import accumulate


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minPrefix = list(accumulate(nums, min))

        stack = []
        n = len(nums)
        
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]: #나보다 작으면? 뒤져야지
                stack.pop()

            if stack and minPrefix[stack[-1]] < nums[i]:
                return True

            if stack and minPrefix[stack[-1]] == minPrefix[i]:
                continue

            stack.append(i) #내림차순을 유지함 #사실
        return False






        return False








s = Solution()
s.find132pattern([1,2,-1,4,5])


