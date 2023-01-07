class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        accum,idx = 0, 0
        
        if sum(gas) < sum(cost):
            return -1
        
        loop = False
        for i in range(len(gas)):
            if loop and idx == i:
                return idx
            
            accum += gas[i] - cost[i]
            
            while accum < 0:
                idx = len(gas) - 1 if not idx else idx - 1
                accum += gas[idx] - cost[idx]
                
            loop = True
                
        print(idx)
        return idx
