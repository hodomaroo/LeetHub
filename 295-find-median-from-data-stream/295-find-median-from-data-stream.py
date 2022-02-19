from heapq import heappop,heappush
class MedianFinder(object):

    def __init__(self):
        self.minHeap = []   #가장 큰 요소들이 저장
        self.maxHeap = []   #가장 작은 요소들이 저장

    def addNum(self, num):

        if len(self.minHeap) < len(self.maxHeap):   heappush(self.minHeap,num)
        else:   heappush(self.maxHeap, -num)

        while self.maxHeap and self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            heappush(self.maxHeap,-heappop(self.minHeap))
            heappush(self.minHeap, -heappop(self.maxHeap))
        #print(self.maxHeap,self.minHeap)

    def findMedian(self):
        if (len(self.minHeap) + len(self.maxHeap)) % 2:
            return float(-self.maxHeap[0])
        elif len(self.minHeap):
            return float(-self.maxHeap[0] + self.minHeap[0]) / 2
        #return None

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()