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


def insert_bst(root,data):
    if root == None:
        node = BinaryTreeNode(data)
        return node

    elif root.data > data:
        root.left = insert_bst(root.left,data)
        

    elif root.data < data:
        root.right = insert_bst(root.right,data)
        
    return root
    
#root = treeInput()
root = None
root = insert_bst(root,2)
root = insert_bst(root,1)
root = insert_bst(root,3)
printTree(root)

