# LeetCode 113. Path Sum II

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        
        if root is None:
            return res
        
        def dfshelper(node,targetSum,slate):
            if node.left is None and node.right is None:
                if node.val == targetSum:
                    
                    slate.append(node.val)
                    
                    res.append(slate[:])
                    slate.pop()
                return
            
            else:
                if node.left:
                    
                    
                    slate.append(node.val)
                    dfshelper(node.left,targetSum-node.val,slate)
                    slate.pop()
                
                if node.right:
                    
                    
                    slate.append(node.val)
                    dfshelper(node.right,targetSum-node.val,slate)
                    slate.pop()
                    
        
        
        dfshelper(root,targetSum,[])
        
        return res