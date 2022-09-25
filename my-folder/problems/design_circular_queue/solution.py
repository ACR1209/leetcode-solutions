class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.size = k
        self.tail = -1
        self.front = -1

    def enQueue(self, value: int) -> bool:
        if self.front == -1:
            self.queue.append(value)
            self.front, self.tail = 0, 0
            return True
        
        if self.isFull():
            return False
        
        self.queue.append(value)
        self.tail = len(self.queue) - 1
        
        return True        
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        del self.queue[0]
        self.tail -= 1 
        
        if self.isEmpty():
            self.front = -1
        
        return True

    def Front(self) -> int:
        return self.queue[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.queue[self.tail] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.tail == -1

    def isFull(self) -> bool:
        return self.tail == self.size - 1
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()