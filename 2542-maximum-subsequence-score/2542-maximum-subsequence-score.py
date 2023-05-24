class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sortedNums = sorted(list(range(len(nums1))), key = lambda idx : nums1[idx])
        keys = sorted(nums2)
        minHeap,total = [],0
        
        ans = 0
        for curV in keys:
            while minHeap and minHeap[0][0] < curV:
                total -= heappop(minHeap)[1]
            
            while  len(minHeap) < k and len(sortedNums) >= (k - len(minHeap)):
                if curV > nums2[sortedNums[-1]]: 
                    sortedNums.pop()
                    continue
                    
                idx = sortedNums.pop()                
                heappush(minHeap, (nums2[idx], nums1[idx]))
                total += nums1[idx]
        
            if len(minHeap) == k:
                ans = max(ans, total * curV)
            
            if len(sortedNums) < (k - len(minHeap)):    break
        return ans
                
        