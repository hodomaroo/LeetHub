from typing import List
from heapq import heappop,heappush

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        usingLadder = []
        count = 0

        #래더개수
        for i in range(1,len(heights)):
            diff = heights[i] - heights[i - 1]
            #print(usingLadder,count)
            
            if diff > 0:
                if ladders == len(usingLadder):
                    if ladders and usingLadder[0] < diff :
                        count += heappop(usingLadder)
                        heappush(usingLadder, diff)
                    else:
                        count += diff
                else:
                    heappush(usingLadder, diff)
            if count > bricks: break
        return i - 1 if count > bricks else i
            
            



