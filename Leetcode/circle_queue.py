# 622. Design Circular Queue
# Design your implementation of the circular queue.

# 1. mine (108 ms)
"""
class MyCircularQueue:
    def __init__(self, k: int):
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = k
        self.que = [None] * k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.que[self.rear] = value
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.que[self.front] = None
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return True

    def Front(self) -> int:
        return -1 if self.que[self.front] is None else self.que[self.front]

    def Rear(self) -> int:
        return -1 if self.que[self.rear - 1] is None else self.que[self.rear-1]

    def isEmpty(self) -> bool:
        return self.no <= 0

    def isFull(self) -> bool:
        return self.no >= self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
"""

# 2. another way (76 ms)
class MyCircularQueue:
    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.capacity = k
        self.que = [None] * k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.que[self.rear] = value
        self.rear  = (self.rear + 1) % self.capacity
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.que[self.front] = None
        self.front = (self.front + 1) % self.capacity
        return True

    def Front(self) -> int:
        return -1 if self.que[self.front] is None else self.que[self.front]

    def Rear(self) -> int:
        return -1 if self.que[self.rear - 1] is None else self.que[self.rear-1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.que[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.que[self.front] is not None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
