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


def distanceK(root,k,res):

        # Check for empty root
        if root is None:
            return
            
        # if k is 0 then add node to res 
        if k == 0:
            res.append(root.data)


        # Call for left subtree and decrement k by 1
        distanceK(root.left,k-1,res)

        # Call for right subtree and decrement k by 1
        distanceK(root.right,k-1,res)


root = treeInput()
k = int(input())
printTree(root)
res = []
distanceK(root,k,res)
print(res)

# Time Complexity O(n) where n are the no of nodes in a tree
# Space Complexity O(h) due to recursion stack