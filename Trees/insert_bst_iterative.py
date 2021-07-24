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


def insert_bst(root,k):

    newNode = BinaryTreeNode(k)

    if root is None:
        return newNode

    prev = None
    curr = root

    while curr is not None:
        if k == curr.data:
            return 'key already exists'

        elif k < curr.data:
            prev = curr
            curr = curr.left

        elif k > curr.data:
            prev = curr
            curr = curr.right


    if k < prev.data:
        prev.left = newNode
    else:
        prev.right = newNode

    return root


root = None
root = insert_bst(root,2)
root = insert_bst(root,1)
root = insert_bst(root,3)

printTree(root)
