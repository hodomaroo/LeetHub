from sortedcontainers import SortedList
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl : SortedList = SortedList()
        count = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            count[i] = sl.bisect_left(nums[i])
            sl.add(nums[i])
            #sl.append(nums[i])
        return count
