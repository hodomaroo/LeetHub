class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        accum,idx = 0, 0
        
        if sum(gas) < sum(cost):
            return -1
        
        for i in range(len(gas)):
            
            accum += gas[i] - cost[i]
            
            while accum < 0:
                idx = len(gas) - 1 if not idx else idx - 1
                accum += gas[idx] - cost[idx]
                
        print(idx)
        return idx
