
LinkedList = []
FirstNode = -1
FirstEmpty = 0


# Exercise 1
def Initialise():
    global FirstNode,FirstEmpty,LinkedList
    LinkedList = []
    FirstNode = -1
    FirstEmpty = 0
    for x in range(10):
        LinkedList.append([-1, x + 1])
    LinkedList[9][1] = -1

def OutputNodes():
    if FirstNode == -1:
        print("Linked list is empty")
    else:
        CurrentNode = FirstNode

        while CurrentNode != -1:
            print(LinkedList[CurrentNode][0])
            CurrentNode = LinkedList[CurrentNode][1]

# Exercise 2
def InsertInOrder(Item):
    global FirstNode, FirstEmpty

    if FirstEmpty == -1:
        return False

    NewNode = FirstEmpty
    FirstEmpty = LinkedList[FirstEmpty][1]
    LinkedList[NewNode][0] = Item

    if FirstNode == -1:
        LinkedList[NewNode][1] = -1
        FirstNode = NewNode
        return True

    if Item < LinkedList[FirstNode][0]:
        LinkedList[NewNode][1] = FirstNode
        FirstNode = NewNode
        return True

    CurrentNode = FirstNode

    while LinkedList[CurrentNode][1] != -1 and LinkedList[LinkedList[CurrentNode][1]][0] <= Item:
        CurrentNode = LinkedList[CurrentNode][1]

    LinkedList[NewNode][1] = LinkedList[CurrentNode][1]
    LinkedList[CurrentNode][1] = NewNode

    return True


# Exercise 3
def Delete(Item):
    # Write your code here
    pass


# Exercise 4
def LoadFromFile(FileName):
    # Write your code here
    pass


# Exercise 5
def Reverse():
    # Write your code here
    pass
