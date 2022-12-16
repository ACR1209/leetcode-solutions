class MyQueue:

    def __init__(self):
        self.store = []
        self.buffer = []


    def push(self, x: int) -> None:
        self.store.append(x)

    def pop(self) -> int:
        while len(self.store) > 1:
            self.buffer.append(self.store.pop())
        current = self.store.pop()

        while len(self.buffer) > 0:
            self.store.append(self.buffer.pop())
        return current         

    def peek(self) -> int:
        return self.store[0]

    def empty(self) -> bool:
        return len(self.store) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()