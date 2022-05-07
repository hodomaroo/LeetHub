from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 or not nums2:
            if not nums1:
                nums1 = nums2
            #길이가 4면 인덱스가 2
            #길이가 3이면 인덱스가 1
            return sum(nums1[len(nums1) // 2 - 1 + len(nums1) % 2: len(nums1) // 2 + 1]) / (2 - len(nums1) % 2)

        def binarySearch(array : List[int], v : int) -> int: #--> v보다 작은 요소의 개수 리턴
            l,r = -1,len(array)
            #0이라는건 1개!
            while l + 1 < r:
                mid = (l + r) // 2
                if array[mid] < v: #--> mid값이 v보다 작다면
                    l = mid
                else:
                    r = mid # -> r >= v를 만족
            return l + 1


        l,r = -(10 ** 6) - 1,10**6 + 1
        total = len(nums1) + len(nums2)

        ans = 0

        while l + 1 < r:
            mid = (l + r) // 2
            x = binarySearch(nums1, mid)
            y = binarySearch(nums2, mid)

            if x + y <= total // 2:
                l = mid
            else:
                r = mid
            #값이 단 하나만 존재한다면? --> left는 존재하는 값이 되어야 함
            # 0 0 0 0
        ans += l
        print(l)

        l,r = -(10 ** 6) - 1,10**6 + 1
        while l + 1 < r:    
            mid = (l + r) // 2
            x = binarySearch(nums1, mid)
            y = binarySearch(nums2, mid)

            if x + y <= total // 2 - 1 + total % 2:
                l = mid
            else:
                r = mid
        
        ans += l
        #값이 단 하나만 존재한다면? 
        # 0 0 0 0 --> 0이면 0개 1이면 4개 
        print(l)
        return ans / 2
        
        
        







