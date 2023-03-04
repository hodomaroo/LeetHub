from typing import List
from collections import deque


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        nums += [0]
        min_vals, max_vals = deque(), deque()
        case, left = 0, 0

        for right in range(len(nums)):
            if nums[right] == minK:
                min_vals.append(right)

            if nums[right] == maxK:
                max_vals.append(right)

            # 현재 위치값이 범위 밖인경우
            if minK > nums[right] or maxK < nums[right]:
                while min_vals and max_vals:  # 현재까지 가능한 케이스를 모두 진행함
                    # 두 값의 가장 왼쪽 위치중 가장 큰것까지는 유효한 케이스라고 볼 수 있음
                    case += right - max(min_vals[0], max_vals[0])
                    left += 1

                    # 유효하지 않은 범위에 있는 값들 제거
                    while min_vals and min_vals[0] < left:
                        min_vals.popleft()

                    while max_vals and max_vals[0] < left:
                        max_vals.popleft()

                left = right + 1
                # print(min_vals, max_vals)
                min_vals.clear()
                max_vals.clear()
                continue
        return case