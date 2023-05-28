class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts) + [n]
        dp = [[10000000] * len(cuts) for _ in range(len(cuts) + 1)]
        #dp[length][first_index]
        dp[1] = [0 for i in range(len(cuts))]
        
        #전체 길이 + 합쳐져야 하는 애들의 길이
        for length in range(2, len(cuts) + 1): #length
            for first_index in range(len(cuts) - length + 1): 
                for mid_index in range(first_index + 1, first_index + length):
                    dp[length][first_index] = min(dp[length][first_index], cuts[first_index + length - 1] - (cuts[first_index - 1] if first_index else 0) + dp[mid_index - first_index][first_index] + dp[length - (mid_index - first_index)][mid_index])
        
        #print(*dp, sep = "\n")
        return min(dp[-1])
            