class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: (x[0] - x[1]))
        #print(costs)
        return sum([costs[i][0] for i in range(len(costs) //2)]) + sum([costs[i][1] for i in range(len(costs) //2,len(costs))])



