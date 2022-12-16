class MyQueue:

    def __init__(self):
        self.left = 0
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.left != len(self.queue):
            self.left += 1
            
        return self.queue[self.left - 1]
        

    def peek(self) -> int:
        return self.queue[self.left]

    def empty(self) -> bool:
        return self.left == len(self.queue)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()