class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cost,heap,capital = w,[], sorted(zip(capital, profits), reverse = True)
        
        for _ in range(k):
            while capital and capital[-1][0] <= cost:
                heappush(heap, -capital.pop()[1])
            
            if heap:    cost += -heappop(heap)
        
        return cost
                
                
            
            
        
        