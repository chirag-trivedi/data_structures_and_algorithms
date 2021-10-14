

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def treeInput():
    rootData = int(input())

    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def printTree(root):
    if root is None:
        return 

    print(root.data,end=":")
    if root.left:
        print("Left=",root.left.data,end=",")
    else:
        print("Left=",None,end=",")
    if root.right:
        print("Right=",root.right.data)
    else:
        print("Right=",None)

    printTree(root.left)
    printTree(root.right)


def height(root):
    if root is None:
        return 0

    lH = height(root.left)
    rH = height(root.right)

    return 1 + max(lH,rH)

def diameter(root):

    globalbox = 0

    if root is None:
        return globalbox

    def dfshelper(root):
        if root.left is None and root.right is None:
            return 0 

        mydia = 0
        if root.left:
            LH = dfshelper(root.left)
            mydia += LH + 1
        if root.right:
            RH = dfshelper(root.right)
            mydia += RH + 1

        globalbox = max(globalbox,mydia)

        return max(LH,RH) + 1

    dfshelper(root)

    return globalbox


root = treeInput()
printTree(root)
print(height(root))
print(diameter(root))