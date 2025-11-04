class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
head = Node(10)
temp = head

temp.next = Node(20)
temp.next.next = Node(30)
temp.next.next.next = Node(40)


# this is the function for traversing the linkedlist
def linkedListTraversal():
    global head
    newTemp = head 
    while newTemp is not None:
        print(newTemp.data,end=" ")
        newTemp = newTemp.next


# function to add a new node at the end of the linkedList
def addNode(data):
    newNode = Node(data)
    newTemp = head
    while newTemp.next is not None:
        newTemp = newTemp.next
    newTemp.next = newNode

# function to add a new node at the beginning of the linkedlist
def addNodeAtBeg(data):
    global head # while reading head variable we don't need to declare it as a global variable, but when we are mofifying it we need to declare it as a glovbal variable
    newNode = Node(data)
    newTemp = head
    newNode.next = newTemp
    head = newNode

#function to add a new node at a specific position
def addNodeAtPosition(data,position):
    global head
    newNode = Node(data)
    newTemp = head
    if position < 1:
        return head
    if position == 1:
        addNodeAtBeg(data)
    for _ in range(1,position-1):
        if newTemp is None:
            return head
        newTemp = newTemp.next
    
    newNode.next = newTemp.next
    newTemp.next = newNode


addNode(50)
addNodeAtBeg(5)
addNodeAtPosition(25,3)


# function to delete a node from the end of the linkedlist
def deleteNodeEnd():
    prev = None
    newTemp = head
    while newTemp.next is not None:
        prev = newTemp
        newTemp = newTemp.next
    
    prev.next= None
    del newTemp

# function to delete a node from the beginning of the linkedlist
def deleteNodeBeg():
    global head
    if head is None:
        return 
    newTemp = head 
    head = newTemp.next
    del newTemp

# function to delete a node from a specific position
def deleteNodeAtPosition(pos):
    global head
    prev = None
    newTemp = head
    if pos<1:
        return head
    if pos==1:
        deleteNodeBeg()
    for _ in range(1,pos-1):
        if newTemp is None:
            return head
        prev = newTemp
        newTemp = newTemp.next
    prev.next = newTemp.next
    del newTemp


# function to search an element in the given linkedlist
def searchElement(data):
    newTemp = head
    elePos = 1

    while newTemp is not None:
        if newTemp.data == data:
            return f"found the element at position {elePos}"
        newTemp = newTemp.next
        elePos += 1
    return "element not found in the linkedlist"

# function for updating the content of the linkedlist 
def updateLinkElement(data,newData):
    global head
    newTemp = head
    while newTemp is not None:
        if newTemp.data == data:
            newTemp.data = newData
            return
        newTemp = newTemp.next
    return "element not found in the linkedlist"


# function to reverse the linkedlist
def reversedLinkedList():
    global head
    newTemp = head
    prev = None
    nextTemp = None
    while newTemp is not None:
        nextTemp = newTemp.next
        newTemp.next = prev
        prev = newTemp
        newTemp = nextTemp
    head = prev
    


print("linkedList after performing all addition operations")
linkedListTraversal()


deleteNodeEnd()
deleteNodeBeg()
deleteNodeAtPosition(3)

print("\nlinkedList after deleting the last node")
linkedListTraversal()

print("\nlinkedlist after performing the search operation")
print(searchElement(30))

print("\nlinkedliist after updating the element of the linkedlist")
updateLinkElement(20,100)
linkedListTraversal()

print("\nlinkedlist after reversing the linkedlist")
reversedLinkedList()
linkedListTraversal()