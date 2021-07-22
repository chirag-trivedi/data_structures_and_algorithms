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
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    return 1 + max(leftHeight,rightHeight)    


def balanced(root):
    if root is None:
        return True

    checkLeftHeight = height(root.left)
    checkRightHeight = height(root.right)

    if abs(checkLeftHeight-checkRightHeight) > 1:
        return False

    isLeftBalanced = balanced(root.left)
    isRightBalanced = balanced(root.right)

    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False
        

root = treeInput()
printTree(root)
print(balanced(root))
    