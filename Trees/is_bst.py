class BinaryTreeNode:
    def __init__(self,data):
        self.val = data
        self.left_ptr = None
        self.right_ptr = None

def treeInput():
    rootData = int(input())

    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left_ptr = leftTree
    root.right_ptr = rightTree
    return root

def printTree(root):
    if root is None:
        return 

    print(root.val,end=":")
    if root.left_ptr:
        print("Left=",root.left_ptr.val,end=",")
    else:
        print("Left=",None,end=",")
    if root.right_ptr:
        print("Right=",root.right_ptr.val)
    else:
        print("Right=",None)

    printTree(root.left_ptr)
    printTree(root.right_ptr)


def isBSTHelper(root):
    
    if root is None:
        return float('inf'),float('-inf'),True
        
 
    leftMin,leftMax,isLeftBST = isBSTHelper(root.left_ptr)
    rightMin,rightMax,isRightBST = isBSTHelper(root.right_ptr)
    
    minimum = min(leftMin,rightMin,root.val)
    maximum = max(leftMax,rightMax,root.val)
    
    isTreeBST = True
    
    if root.val < leftMax or root.val > rightMin:
        isTreeBST = False
        
    if not isLeftBST or not isRightBST:
        isTreeBST = False
        
    return minimum,maximum,isTreeBST
    
def isBST(root):
     minimum,maximum,isTreeBST = isBSTHelper(root)
     print(isTreeBST)


root = treeInput()
printTree(root)
isBST(root)

    
    