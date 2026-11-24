
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
    # Write your code here
    pass


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
