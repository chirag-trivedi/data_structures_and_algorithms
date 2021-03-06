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


def sum_of_nodes(root):
    if root is None:
        return 0
    
    leftSum = sum_of_nodes(root.left)
    rightSum = sum_of_nodes(root.right)

    return root.data + leftSum + rightSum



root = treeInput()
printTree(root)
print(sum_of_nodes(root))