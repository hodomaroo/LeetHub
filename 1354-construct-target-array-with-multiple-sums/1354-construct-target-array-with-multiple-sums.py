from typing import List
from heapq import heappop, heappush, heapify
from math import ceil

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        target = [-v for v in target]
        if len(target) == 1:
            return target[0] == -1

        heapify(target)

        while True:
            #print(total,target)

            if total <= len(target):
                #print("C")
                return abs(target[0]) == 1 and total == len(target)

            node = abs(heappop(target))
            second = abs(target[0])
            if node == second: 
                
                return False

            diff = total - node
            mod = ceil((node - second) / diff)
            

            heappush(target, -(node - diff * mod))
            total -= diff * mod
S = Solution()
S.isPossible([9,3,5])