class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    @staticmethod
    def createLinkedList(arr):
        head = Node(0)
        dummy = head
        for i in arr:
            dummy.next = Node(i)
            temp = dummy
            dummy = dummy.next
            dummy.prev = temp
        head = head.next
        if head:
            head.prev = None
        return head

linkedList = Node.createLinkedList([1,2,3,4,5])

def printList(head):
    print("List from forwards")
    dummy = head
    temp = None
    while dummy:
        print(dummy.data,end=" ")
        temp = dummy
        dummy = dummy.next
    print("\n")
    print("List from backwards")
    dummy = temp
    while dummy:
        print(dummy.data,end=" ")
        dummy = dummy.prev


def reverseDLL(head):
    dummy = head
    while dummy.next:
        dummy = dummy.next
    
    dummy2 = head
    while dummy2.next:
        temp = dummy2.data
        dummy2.data = dummy.data
        dummy.data = temp
        dummy = dummy.next
        dummy2 = dummy2.next
    return head

head = reverseDLL(linkedList)
printList(head)