class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ssum = sum(v for v in nums if not v % 2)
        ans = []
        
        for v,i in queries:
            if (nums[i] + v) % 2 == 0: 
                ssum += v + ((nums[i] % 2) * nums[i])
                
            elif nums[i] % 2 == 0:
                ssum -= nums[i]
            
            nums[i] += v
            ans.append(ssum)
        return ans