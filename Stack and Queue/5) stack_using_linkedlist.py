class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        # if not self.head:
        #     self.head = Node(data)
        #     return
        # temp = self.head
        # temp.next = Node(data)
        # temp = temp.next
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        temp = self.head
        dummy = None
        while temp.next is not None:
            dummy = temp
            temp = temp.next
        print(temp.data)
        dummy.next = None
    
    def top(self):
        temp = self.head
        dummy = None
        while temp.next is not None:
            temp = temp.next
        print(temp.data)
        
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.pop()
stack.top()