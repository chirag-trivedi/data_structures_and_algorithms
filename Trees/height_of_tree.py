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

    leftHt = height(root.left)
    rightHt = height(root.right)

    return max(leftHt,rightHt) + 1


root = treeInput()
printTree(root)
print(height(root))

# Time Complexity O(n) where n are the no of nodes in a tree
# Space Complexity O(n) due to recursion stack