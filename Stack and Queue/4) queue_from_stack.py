from collections import deque

class Queue:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def enqueue(self,x):
        self.q1.append(x)

    def dequeue(self):
        if not self.q1:
            print("Queue Empty")
            return None
        
        while len(self.q1)>1:
            self.q2.append(self.q1.popleft())
        
        item = self.q1.popleft()
        print(item)
        
        self.q1, self.q2 = self.q2, self.q1
        return item

    def top(self):
        if not self.q1:
            print("queue Empty")
            return None
        
        item = self.q1[0]
        print(item)
        return item
    
    def empty(self):
        if self.q1 == 0:
            print("Empty queue")
        else:
            print("queue Not Empty")
    
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.dequeue()
queue.top()
queue.dequeue()
queue.top()
queue.empty()