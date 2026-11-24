
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
    print(LinkedList[0][0])
    for i in range(len(LinkedList)-1,1,1):
        print(LinkedList[LinkedList[i][1]][0])


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
