from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1] * len(ratings)
        right = [1] * len(ratings)

        for i in range(1, len(ratings)):
            left[i] = (left[i - 1] + 1) if ratings[i] > ratings[i - 1] else 1
            right[-i - 1] = (right[-i] + 1) if ratings[-i - 1] > ratings[-i] else 1

        return sum(max(left[i], right[i]) for i in range(len(ratings)))




