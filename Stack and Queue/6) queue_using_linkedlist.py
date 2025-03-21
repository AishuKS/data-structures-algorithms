class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        
    def enqueue(self, data):
        if not self.head:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)
    
    def dequeue(self):
        temp = self.head
        dummy = None
        while temp.next is not None:
            dummy = temp
            temp = temp.next
        print(temp.data)
        dummy.next = None
    
    def front(self):
        temp = self.head
        dummy = None
        while temp.next is not None:
            temp = temp.next
        print(temp.data)
        
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.dequeue()
queue.front()