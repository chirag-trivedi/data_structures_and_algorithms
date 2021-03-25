class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


def printLL(head):
    while head is not None:
        print(head.data,end="-->")
        head = head.next
    print('None')


def takeInput():
    inputList = [int(i) for i in input().split()]

    head = None
    for currData in inputList:
        if currData == -1:
            break
        else:
            newNode = Node(currData)
            if head is None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode

    return head

head = takeInput()
printLL(head)