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



# function for inserting the node at the begining of the doubly linkedlist

def insertAtBeg(data):
    global head
    newTemp = head
    newNode = Node(data)
    newNode.next = newTemp
    newNode.prev = None
    if newTemp is not None:
        newTemp.prev = newNode
    head = newNode

# function for inserting the node at the end of the doubly linkedlist
def insertAtEnd(data):
    global head
    newTemp = head
    newNode = Node(data)

    if newTemp is None:
        head = newNode
        return head
    while newTemp.next is not None:
        newTemp = newTemp.next

    newTemp.next = newNode
    newNode.prev = newTemp
    newNode.next = None

# fucntion to insert the at the given position in the doubly linkedlist
def insertAtPos(data,pos):
    newTemp = head
    newNode = Node(data)

    if pos<1:
        return head
    if pos==1:
        insertAtBeg(data)
    for _ in range(1,pos-1):
        if newTemp is None:
            return head
        newTemp = newTemp.next
    newNode.next = newTemp.next 
    newNode.prev = newTemp
    newTemp.next = newNode

# function for deleting the node from the beigning
def deleteAtBeg():
    global head
    newTemp = head
    head = newTemp.next
    head.prev = None
    del newTemp

    


doublyLinkedListTraverse()
# print("\nReading the linkedlist backwards")
# readingBackWards()
# print("\nDoubly linkedlist after reversing it")
# reversingDoublyLinkedList()
# doublyLinkedListTraverse()

insertAtBeg(5)
insertAtEnd(50)
insertAtPos(60,3)
print("\n linkedlist after performing all the addition operations.......")
doublyLinkedListTraverse()
print("\n")
deleteAtBeg()
doublyLinkedListTraverse()
