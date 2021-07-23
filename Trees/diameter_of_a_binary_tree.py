

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

    if root is None:
        return 0

    d1 = 1 + height(root.left) + height(root.right)

    d2 = diameter(root.left)

    d3 = diameter(root.right)

    return max(d1,max(d2,d3))


root = treeInput()
printTree(root)
print(height(root))
print(diameter(root))