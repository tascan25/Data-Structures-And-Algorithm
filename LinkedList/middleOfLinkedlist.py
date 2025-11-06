class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(1)
temp = head

temp.next = Node(2)
temp.next.next = Node(3)
temp.next.next.next = Node(4)
temp.next.next.next.next = Node(5)
temp.next.next.next.next.next = Node(6)

def linkTraverseal():
    tempv = head
    while tempv is not None:
        print(tempv.data,end=" ")
        tempv = tempv.next

def findLinkLength():
    tempv = head
    no_of_node = 0
    length = 0
    while tempv is not None:
        no_of_node = no_of_node+1
        tempv = tempv.next
    length = no_of_node
    return length

def removeAtBeg():
    global head
    tempv = head
    head = tempv.next
    del tempv
    return head

def findMiddleElement():         # BRUTE FORCE APPROACH
    tempv = head
    tempArray = []

    while tempv is not None:
        tempArray.append(tempv.data)
        tempv = tempv.next
    
    array_length = len(tempArray)
    middle_Element_Index = array_length//2
    middle_Element = tempArray[middle_Element_Index]
    return middle_Element

def middleELementDoubleTraversal():
    tempv = head
    count = 0
    middle = head
    while tempv is not None:
        count+=1
        tempv = tempv.next
    i=0
    while i<(count//2):
        middle = middle.next
        i+=1
    
    return middle.data

def middleElementSingleTraversal():
    tempv = head
    count = 0
    middle = head

    while tempv is not None:
        count+=1
        if(count%2==0):
            middle = middle.next
        tempv = tempv.next

    return middle.data

def middle_slow_fast_pointer():
    slow = head
    fast  = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.data



print("Linkedlist is -> ")
linkTraverseal()
middle1 = findMiddleElement()
middle2 = middleELementDoubleTraversal()
middle3 = middleElementSingleTraversal()
middle4 = middle_slow_fast_pointer()
print("\n the middle element of the linkedlist is -> ",middle4)
findMiddleElement()