class NumArray:

    def __init__(self, nums: List[int]):
        self.depth = ceil(log2(len(nums)))
        self.segmentTree = [0] * pow(2, self.depth + 1)
        self.baseNodes = pow(2, self.depth)
        
        for i in range(len(nums)):
            self.update(i, nums[i])

    def update(self, index: int, val: int) -> None:
        index = len(self.segmentTree) - self.baseNodes + index
        
        self.segmentTree[index] = val
        
        while index:
            index >>= 1
            
            self.segmentTree[index] = self.segmentTree[index << 1] + self.segmentTree[(index << 1) | 1]     
#        print(self.segmentTree)
            

    def sumRange(self, left: int, right: int) -> int:
        
        def getSegmentValue(index : int, lower : int, upper : int, left : int, right : int) -> int:   
            if left == lower and right == upper:
                return self.segmentTree[index]
            
            mid = lower + (upper - lower) // 2
            
            value = 0
            
            if left < mid: # [left , mid)
                value += getSegmentValue(index << 1, lower, mid, left, min(right,mid))
            
            if right > mid:# [mid, right)
                value += getSegmentValue((index << 1) | 1, mid, upper , max(mid, left) , right) 
            return value
        
        
        return getSegmentValue(1, 0, self.baseNodes, left, right + 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)