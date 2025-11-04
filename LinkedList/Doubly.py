class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

head = Node(10)
head.prev = None
temp = head

temp.next = Node(20)
temp.next.prev = temp

temp.next.next = Node(30)
temp.next.next.prev = temp.next

temp.next.next.next = Node(40)
temp.next.next.next.prev = temp.next.next

# function for the doubly linkedlist traversal
def doublyLinkedListTraverse():
    newTemp = head
    while newTemp is not None:
        print(newTemp.data, end=" ")
        newTemp = newTemp.next

# function for reading the doubly linkedlist backwards
def readingBackWards():
    global head
    newTemp = head
    while newTemp.next is not None:
        newTemp = newTemp.next
    head = newTemp
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.prev

# function for reversing the doubly linkedlist

def reversingDoublyLinkedList():
    global head
    newTemp = head
    prevNode = None
    while newTemp is not None:
        nextNode = newTemp.next
        newTemp.next = prevNode
        newTemp.prev = nextNode
        prevNode = newTemp
        newTemp = nextNode
    head = prevNode



doublyLinkedListTraverse()
print("\nReading the linkedlist backwards")
readingBackWards()
print("\nDoubly linkedlist after reversing it")
reversingDoublyLinkedList()
doublyLinkedListTraverse()