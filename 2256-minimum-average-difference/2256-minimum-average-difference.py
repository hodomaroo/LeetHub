class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix = list(accumulate(nums))
        return min(list(range(len(nums))),key = lambda i : (abs(prefix[i] // (i + 1) - (0 if i + 1 == len(nums) else ((prefix[-1] - prefix[i]) // (len(nums) - i - 1)))),i))