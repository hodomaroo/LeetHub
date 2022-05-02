from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numPos = dict()
        nextOfNums = [-1] * len(nums2)

        for i in range(len(nums2)):
            numPos[nums2[i]] = i

        stack = []
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                nextOfNums[numPos[stack.pop()]] = nums2[i]
            stack.append(nums2[i]) #값 추가하기

        #print(nextOfNums)
        return [nextOfNums[numPos[v]] for v in nums1]
