class Solution:
    def insert(self, intervals: List[List[int]], b: List[int]) -> List[List[int]]:
        def function(a):
            return (a[0] >= b[0] and a[1] < b[1]) or (a[0] <= b[0] and a[1] >= b[1]) or (a[0] >= b[0] and a[0] <= b[1]) or (a[1] >= b[0] and a[1] <= b[1])
        
        inter = list(filter(function, intervals))
        
        if not inter:
            node = bisect_left(intervals, b[0], key = lambda x : x[1])
            return intervals[:node] + [b] + intervals[node:]
        
        intervals[intervals.index(inter[0]):intervals.index(inter[-1]) + 1] = [[min(inter[0][0], b[0]), max(b[1], inter[-1][1])]]
        return intervals
        
        

        
        