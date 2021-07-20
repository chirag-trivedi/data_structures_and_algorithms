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


def mirror(root):

    if root is None:
        return

    if root.left is None and root.right is None:
        return root

    elif root.left is not None and root.right is not None:
        root.left,root.right = root.right, root.left

    elif root.left is not None and root.right is None:
        root.left,root.right = None, root.left

    elif root.left is None and root.right is not None:
        root.left,root.right = root.right, None

    mirror(root.left)
    mirror(root.right)

    return root

root = treeInput()
printTree(root)
root = mirror(root)
printTree(root)

# Time Complexity O(n) where n are the no of nodes in a tree
# Space Complexity O(n) due to recursion stack