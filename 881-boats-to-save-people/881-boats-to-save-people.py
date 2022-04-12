from typing import List
from bisect import bisect_right #탈수있는 가장 무거운 사람
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 가장 무거운 사람부터 / 매칭되는 가장 무거운 사람과 함께 가기
        people.sort()
        isValid = [True] * len(people)
        remain = len(people)
        count = 0

        limitIndex = len(people)

        for i in range(len(people)):
            if not isValid[i]: continue
            
            target = bisect_right(people,limit - people[i] , lo=i + 1, hi=limitIndex) - 1
            if target > i:  isValid[target] = False

            limitIndex = target
            count += 1


        return count
print(bisect_right([1,2,3,4,5],5,hi=4))




