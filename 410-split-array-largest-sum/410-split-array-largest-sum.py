from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums)-1, 10**9

        while left + 1 < right:
            mid = (left + right) // 2
            #print(mid)
            tot, cnt = 0, 0
            for v in nums:
                tot += v
                if tot > mid:
                    tot,cnt = v,cnt + 1
            cnt += (tot > 0)

            if cnt <= m:
                right = mid #cnt가 작거나 같을때까지 계속 작아짐
            else: #cnt가 mid보다 작다는건 좀 더 키워야 한다는 소리
                left = mid #left는 cnt가 더 큼

        return right
