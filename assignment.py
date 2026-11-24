LinkedList = []
FirstNode = -1
FirstEmpty = 0


# Exercise 1
def Initialise():
    global FirstNode, FirstEmpty, LinkedList
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
    global FirstNode, FirstEmpty

    CurrentNode = FirstNode
    PreviousNode = -1

    while CurrentNode != -1 and LinkedList[CurrentNode][0] != Item:
        PreviousNode = CurrentNode
        CurrentNode = LinkedList[CurrentNode][1]

    if CurrentNode == -1:
        return False

    if PreviousNode == -1:
        FirstNode = LinkedList[CurrentNode][1]
    else:
        LinkedList[PreviousNode][1] = LinkedList[CurrentNode][1]

    LinkedList[CurrentNode][0] = -1
    LinkedList[CurrentNode][1] = FirstEmpty
    FirstEmpty = CurrentNode

    return True


# Exercise 4
def LoadFromFile(FileName):
    global FirstNode, FirstEmpty

    Initialise()
    Count = 0

    try:
        File = open(FileName, "r")

        for Line in File:
            Item = int(Line)

            if InsertInOrder(Item):
                Count += 1
            else:
                break

        File.close()
        return Count

    except FileNotFoundError:
        print("File not found")
        return -1


# Exercise 5
def Reverse():
    global FirstNode

    Previous = -1
    Current = FirstNode

    while Current != -1:
        NextNode = LinkedList[Current][1]
        LinkedList[Current][1] = Previous
        Previous = Current
        Current = NextNode

    FirstNode = Previous
