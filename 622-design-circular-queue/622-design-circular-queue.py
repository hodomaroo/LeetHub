class MyCircularQueue:

    def __init__(self, k: int):
        self.fullFlag = False
        self.front = 0
        self.rear = 0
        self.queue = [None for _ in range(k)]
        self.queueSize = k

    def enQueue(self, value: int) -> bool:
        if self.fullFlag:   return False
        
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.queueSize
        
        self.fullFlag = self.rear == self.front
        
        return True

    def deQueue(self) -> bool:
        if not self.fullFlag and self.front == self.rear:   return False
        
        self.front = (self.front + 1) % self.queueSize
        self.fullFlag = False 
        
        return True
    
    def Front(self) -> int:
        return -1 if not self.fullFlag and self.front == self.rear else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if not self.fullFlag and self.front == self.rear else self.queue[(self.rear + self.queueSize - 1) % self.queueSize]

    def isEmpty(self) -> bool:
        return not self.fullFlag and self.front == self.rear

    def isFull(self) -> bool:
        return self.fullFlag


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()