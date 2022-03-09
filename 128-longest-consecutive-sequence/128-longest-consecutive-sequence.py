
class Solution(object):
    def __init__(self):
        self.maxSize = 1

    def longestConsecutive(self,nums):
        if not nums: return 0
        parent = {v: [v, 1] for v in nums}
        #length = {v : 1 for v in nums}

        def union(a,b):
            global maxSize
            if isUnion(a,b): return
            parent[parent[b][0]][1] += parent[parent[a][0]][1]
            parent[parent[a][0]][0] = parent[b][0]
            self.maxSize = max(self.maxSize,parent[parent[b][0]][1])
            return

        def getParent(a):
            if parent[a][0] == a:  return a

            parent[a][0] = getParent(parent[a][0])
            return parent[a][0]

        def isUnion(a,b):
            return getParent(a) == getParent(b)

        for v in nums:
            if v+1 in parent: union(v,v+1)

        return self.maxSize

S = Solution()
print(S.longestConsecutive([0]))





