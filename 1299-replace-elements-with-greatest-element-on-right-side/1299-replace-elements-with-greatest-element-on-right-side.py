class Solution(object):
    def replaceElements(self, arr):
        maxValue = -1
        soluiton = [0] * len(arr)
        for i in range(len(arr)-1,-1,-1):
            soluiton[i] = maxValue
            maxValue = max(maxValue,arr[i])
        return soluiton

