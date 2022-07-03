from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [[1, 1] for _ in range(len(nums))]
        #0 -> positive / 1 -> negative
        maxLen = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] == nums[j]: continue
                print(nums[i] < nums[j],i,j)
                dp[i][nums[i] < nums[j]] = max(dp[i][nums[i] < nums[j]], dp[j][1 - (nums[i] < nums[j])] + 1)
                maxLen = max(maxLen, dp[i][nums[i] < nums[j]])
        return maxLen

