import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)

        num_arr = [[nums2[i], nums1[i]] for i in range(n)]
        num_arr.sort(key = lambda x:x[0], reverse = True)

        curr_sum = 0
        heap = []

        for i in range(k):
            curr_sum += num_arr[i][1]
            heapq.heappush(heap, num_arr[i][1])
        
        final_ans = num_arr[k-1][0]*curr_sum

        for i in range(k, n):
            curr_num2 = num_arr[i][0]
            curr_num1 = num_arr[i][1]

            min_heap_ele = heapq.heappop(heap)

            if curr_num1 > min_heap_ele:
                heapq.heappush(heap, curr_num1)
                curr_sum -= min_heap_ele
                curr_sum += curr_num1
            else:
                heapq.heappush(heap, min_heap_ele)
            
            final_ans = max(final_ans, curr_num2*curr_sum)
        
        return final_ans