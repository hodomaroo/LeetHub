
class Solution(object):
    def __init__(self):
        self.maxSize = 1
        
    def longestConsecutive(self,nums):
        if not nums: return 0
        parent = {v : v for v in nums}
        length = {v : 1 for v in nums}

        def union(a,b):
            global maxSize
            if isUnion(a,b): return
            length[parent[b]] += length[parent[a]]
            parent[parent[a]] = parent[b]
            self.maxSize = max(self.maxSize,length[parent[b]])

            return

        def getParent(a):
            if parent[a] == a:  return a

            parent[a] = getParent(parent[a])
            return parent[a]

        def isUnion(a,b):
            return getParent(a) == getParent(b)

        for v in nums:
            if v+1 in parent: union(v,v+1)

        return self.maxSize

S = Solution()
print(S.longestConsecutive([0]))





