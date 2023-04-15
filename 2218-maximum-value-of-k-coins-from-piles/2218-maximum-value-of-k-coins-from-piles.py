
from typing import List
from itertools import accumulate


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [[0] * (k) for _ in range(len(piles))]
        prefix = [list(accumulate(piles[i])) for i in range(len(piles))]

        dp[0][0:k] = prefix[0][:min(k, len(piles[0]))] + \
            [0] * (max(k - len(piles[0]), 0))

        for i in range(1, len(piles)):
            # min(j + 1, 파일 길이) 중에 더 작은거만큼
            for j in range(k):
                dp[i][j] = dp[i-1][j]
                # 총 j개를 사용할거임 #0도 한개 사용임
                for w in range(min(j + 1, len(piles[i]))):
                    dp[i][j] = max(dp[i][j], (dp[i - 1]
                                   [j - w - 1] if (j - w - 1 >= 0) else 0) + prefix[i][w])
        #print(*dp, sep="\n")
        return max(dp[i][k-1] for i in range(len(piles)))


s = Solution()
s.maxValueOfCoins(
    [[37, 88], [51, 64, 65, 20, 95, 30, 26], [9, 62, 20], [44]],
    9)
