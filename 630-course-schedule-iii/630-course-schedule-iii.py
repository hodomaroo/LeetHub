from typing import List
from heapq import heappop,heappush
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x : x[1])
        heap = []
        total = 0
        for dur, li in courses:
            #print(heap,total,dur,li)
            if total + dur > li:
                if heap and abs(heap[0][0]) > dur:
                    total += dur - (abs(heap[0][0]) if heap else 0)
                    heappop(heap)
                    heappush(heap,(-dur, li))
            else:
                total += dur
                heappush(heap,(-dur, li))
        return len(heap)