class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.heap = []
        self.dict = {}
        self.countDict = {}
        self.flowDict = {}
        self.flow = 0

    def get(self, key: int) -> int:
        if key in self.dict:
            self.countDict[key] += 1
            self.flowDict[key] = self.flow
            heappush(self.heap, (self.countDict[key], self.flow, key))
            self.flow += 1
        
            return self.dict[key]
        return -1

    def put(self, key: int, val: int) -> None:
        if key in self.dict:
            self.dict[key] = val
            self.flowDict[key] = self.flow
            self.countDict[key] += 1
            heappush(self.heap, (self.countDict[key], self.flow, key))
            self.flow += 1
            return

        if(len(self.dict) == self.cap) and key not in self.dict:
            while self.heap:
                count, idx, value = heappop(self.heap)
                if value not in self.dict or count != self.countDict[value] or self.flowDict[value] != idx : continue

                self.countDict.pop(value)
                self.dict.pop(value)
                self.flowDict.pop(value)
    
                break
        
        if len(self.dict) < self.cap:
            self.dict[key] = val
            self.countDict[key] = 1
            heappush(self.heap, (1, self.flow,  key))
            self.flowDict[key] = self.flow
            self.flow += 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)