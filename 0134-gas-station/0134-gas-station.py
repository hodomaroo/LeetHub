class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        accum,idx = 0, 0
        
        for i in range(len(gas)):    
            if i and idx == i:
                return idx if accum >= 0 else -1
            
            accum += gas[i] - cost[i]
            
            while accum < 0:
                idx = len(gas) - 1 if not idx else idx - 1
                accum += gas[idx] - cost[idx]
                
                if i == idx and accum < 0:
                    return -1
        
            
        return 0
        