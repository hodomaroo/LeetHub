from bisect import bisect_left

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, 2 ** 31

        while l + 1 < r:
            m = (l + r) // 2
            if (m * (m + 1)) // 2 <= n:
                l = m
            else:
                r = m
        return l



