from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self,x):
        self.q1.append(x)

    def pop(self):
        if not self.q1:
            print("Stack Empty")
            return None
        
        while len(self.q1)>1:
            self.q2.append(self.q1.popleft())
        
        item = self.q1.popleft()
        print(item)
        
        self.q1, self.q2 = self.q2, self.q1
        return item

    def top(self):
        if not self.q1:
            print("Stack Empty")
            return None
        
        # while len(self.q1)>1:
        #     self.q2.append(self.q1.popleft())
        
        item = self.q1[-1]
        print(item)
        return item
    
    def empty(self):
        if self.q1 == 0:
            print("Empty Stack")
        else:
            print("Stack Not Empty")
    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.pop()
stack.top()
stack.pop()
stack.top()
stack.empty()