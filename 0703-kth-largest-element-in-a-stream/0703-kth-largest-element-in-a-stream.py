class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.MAX_SIZE = k
        self.heap = []
        
        for v in nums:
            self.add(v)

    def add(self, val: int) -> int:
        if len(self.heap) < self.MAX_SIZE:
            heappush(self.heap, val)
        else:
            if self.heap[0] < val:
                heappop(self.heap)
                heappush(self.heap, val)
        return self.heap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)