from heapq import heappop, heappush
from collections import Counter, defaultdict


# frequency : Heap
# order : Queue

class FreqStack:
    def isValid(self, node: tuple):
 #       print(node)
        return (self.valueStackDict[node[2]] and -node[0] == len(self.valueStackDict[node[2]]) and node[1] ==
                self.valueStackDict[node[2]][-1])

    def __init__(self):
        self.heap = []  # 값이 추가되면 그때 카운트를 추가해서 넣어줌
        self.valueStackDict = defaultdict(list)
        self.count = 0

    def push(self, val: int) -> None:
        self.valueStackDict[val].append(self.count)
        heappush(self.heap, (-len(self.valueStackDict[val]), self.valueStackDict[val][-1], val))

        self.count -= 1
        # 빈도 / 등장 번째로 구현?

    def pop(self) -> int:
        #print(self.heap,self.valueStackDict)
        while not self.isValid(self.heap[0]):  # 등장 횟수 일치 & 등장 순서 일치
#            print(self.heap, self.valueQueueDict)
            heappop(self.heap)

        fre, pos, val = heappop(self.heap)

        self.valueStackDict[val].pop()

        return val