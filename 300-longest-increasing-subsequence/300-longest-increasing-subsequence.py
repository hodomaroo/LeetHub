class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        minValuePerLength = []
        
        for v in nums:
            pos = bisect_left(minValuePerLength,v)
            if pos >= len(minValuePerLength):
                minValuePerLength.append(v)
            else:
                minValuePerLength[pos] = v
            #print(minValuePerLength)
        return len(minValuePerLength)
            
            