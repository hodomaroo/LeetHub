from typing import List
from heapq import heappop,heappush
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #Sweeping Problem
        heap = []
        for num,s,e in trips:
            heappush(heap,(s, num)) #최대한 내리고 태우기
            heappush(heap,(e, -num))
        
        count = 0
        while heap:
            pos = heap[0][0]
            while heap and heap[0][0] == pos:
                p,v = heappop(heap)
                count += v
            if count > capacity:
                return False
        return True
            

        
        
