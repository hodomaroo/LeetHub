class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sortedNums = sorted(zip(nums1, nums2))
        keys = sorted(nums2)
        minHeap,total = [],0
        
        ans = 0
        for curV in keys:
            while minHeap and minHeap[0][0] < curV:
                total -= heappop(minHeap)[1]
            
            while  len(minHeap) < k and len(sortedNums) >= (k - len(minHeap)):
                if curV > sortedNums[-1][1]: 
                    sortedNums.pop()
                    continue
                    
                v, v2 = sortedNums.pop()
                heappush(minHeap, (v2, v))
                total += v
        
            if len(minHeap) == k:
                ans = max(ans, total * curV)
            
        return ans
                
        