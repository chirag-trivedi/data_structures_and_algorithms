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


def bst_search(root,x):
    if root is None:
        return

    if x == root.data:
        return 'Found'

    elif x < root.data:
        return bst_search(root.left,x)

    elif x > root.data:
        return bst_search(root.right,x)


root = treeInput()
printTree(root)
print(bst_search(root,4))
