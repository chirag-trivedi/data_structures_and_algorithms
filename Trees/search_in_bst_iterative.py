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


def search_in_bst(root,x):
    if root is None:
        return 'Not Found'

    curr = root

    while curr is not None:
        if curr.data == x:
            return 'Found'

        elif curr.data > x:
            curr = curr.left

        elif curr.data < x:
            curr = curr.right

    return 'Not Found'


root = treeInput()
printTree(root)
print(search_in_bst(root,4))